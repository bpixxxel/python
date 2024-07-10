import os
import hashlib
import ui

def file_hash(filepath):
    """Generate SHA-256 hash for a given file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def check_integrity(file_paths, alert_function):
    """Check the files for changes and alert if any."""
    hashes = {file: file_hash(file) for file in file_paths}
    try:
        with open('hashes.txt', 'r') as f:
            old_hashes = eval(f.read())
    except FileNotFoundError:
        old_hashes = {}

    for file, new_hash in hashes.items():
        if file in old_hashes and old_hashes[file] != new_hash:
            alert_function(f"Alert: File changed: {file}")

    with open('hashes.txt', 'w') as f:
        f.write(str(hashes))

def alert(message):
    """Display an alert message in the GUI."""
    alert_view = ui.TextView(frame=(0, 0, 320, 240))
    alert_view.text = message
    alert_view.present('sheet')

def main_view():
    """Create the main view of the IDS app."""
    view = ui.View(frame=(0, 0, 320, 480), background_color='white')
    button = ui.Button(title='Check File Integrity')
    button.center = (view.width * 0.5, view.height * 0.5)
    button.flex = 'LRTB'
    button.action = lambda sender: check_integrity(['script1.py', 'script2.py'], alert)
    view.add_subview(button)
    view.present('sheet')

if __name__ == '__main__':
    main_view()
