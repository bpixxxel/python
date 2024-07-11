import zlib
import console

def compute_crc32(data):
    if isinstance(data, str):
        data = data.encode()  # Convert to bytes if input is a string
    return zlib.crc32(data)

def main():
    data = console.input_alert("Input Data", "Enter the data to compute CRC32 checksum:")
    crc32_result = compute_crc32(data)
    print(f"CRC32 Checksum of '{data}': {crc32_result}")

if __name__ == "__main__":
    main()
