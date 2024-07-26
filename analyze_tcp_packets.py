from collections import defaultdict
from pprint import pprint

def analyze_tcp_packets(packets):
    summary = {
        'total_packets': 0,
        'S': 0,
        'A': 0,
        'F': 0,
        'R': 0,
        'P': 0,
        'U': 0,
        'multiple_flags': 0,
        'single_flag': 0,
        'sequence_gaps': 0
    }

    ip_stats = defaultdict(lambda: {'S': 0, 'A': 0, 'F': 0, 'R': 0, 'P': 0, 'U': 0, 'total': 0, 'sequence_numbers': []})
    unusual_combinations = []

    for packet in packets:
        flags = packet['flags']
        ip = packet.get('ip', 'unknown')
        sequence_number = int(packet['sequence_number'])
        summary['total_packets'] += 1
        ip_stats[ip]['total'] += 1
        ip_stats[ip]['sequence_numbers'].append(sequence_number)

        # Count individual flags
        for flag in flags:
            if flag in summary:
                summary[flag] += 1
                ip_stats[ip][flag] += 1

        # Count multiple and single flags
        if len(flags) > 1:
            summary['multiple_flags'] += 1
            unusual_combinations.append((ip, flags))
        else:
            summary['single_flag'] += 1

    # Detect sequence gaps
    for ip, stats in ip_stats.items():
        sequence_numbers = sorted(stats['sequence_numbers'])
        for i in range(1, len(sequence_numbers)):
            if sequence_numbers[i] != sequence_numbers[i - 1] + 1:
                summary['sequence_gaps'] += 1
                break

    # Identify potential SYN flood attacks
    potential_syn_floods = {ip: stats for ip, stats in ip_stats.items() if stats['S'] > 1000}

    # Identify high RST packet rates
    high_rst_rate = {ip: stats for ip, stats in ip_stats.items() if stats['R'] > 500}

    security_report = {
        'Summary': summary,
        'Potential SYN Floods': potential_syn_floods,
        'High RST Rate': high_rst_rate,
        'Unusual Combinations': unusual_combinations
    }

    return security_report

def parse_packet_file(filename):
    packets = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                sequence_number, flags, ip = parts
                packets.append({'sequence_number': sequence_number, 'flags': flags, 'ip': ip})
    return packets

def main():
    filename = input("Enter the filename containing packet data: ")
    packets = parse_packet_file(filename)
    security_report = analyze_tcp_packets(packets)
    pprint(security_report)

if __name__ == "__main__":
    main()
