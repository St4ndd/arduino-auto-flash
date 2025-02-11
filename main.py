import subprocess
import sys
import os
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    arduino_ports = []

    for port in ports:
        if "Arduino Leonardo" in port.description:
            arduino_ports.append(port.device)

    if not arduino_ports:
        print("No Arduino Leonardo found.")
        return None
    elif len(arduino_ports) == 1:
        print(f"Arduino Leonardo found on {arduino_ports[0]}")
        return arduino_ports[0]
    else:
        print("More the one arduino found:")
        for i, port in enumerate(arduino_ports):
            print(f"{i + 1}: {port}")
        choice = int(input("Wähle den Port (1, 2, ...): ")) - 1
        return arduino_ports[choice]

def upload_hex(hex_file_path, port, fqbn="arduino:avr:leonardo"):
    # Pfad zur avrdude.exe (relativ zum Skript)
    AVRDUDE_PATH = os.path.join(os.path.dirname(__file__), "avrdude.exe")
    AVRDUDE_CONF = os.path.join(os.path.dirname(__file__), "avrdude.conf")

    # Upload-Befehl
    upload_cmd = [
        AVRDUDE_PATH,
        "-C", AVRDUDE_CONF,  # Konfigurationsdatei
        "-v",
        "-p", "atmega32u4",   # Prozessor
        "-c", "avr109",       # Programmer-Typ
        "-P", port,           # Port
        "-b", "57600",        # Baudrate
        "-D",
        "-U", f"flash:w:{hex_file_path}:i"
    ]

    # Führe avrdude aus
    upload_result = subprocess.run(
        upload_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if upload_result.returncode != 0:
        print("Error uploading.", upload_result.stderr, file=sys.stderr)
        return False

    print("Scetch uploaded successfully!")
    return True

if __name__ == "__main__":
    HEX_FILE_PATH = "/blink.hex"  

    PORT = find_arduino_port()
    if not PORT:
        print("No Arduino Leonardo found. Please check the connection.")
        sys.exit(1)

    success = upload_hex(HEX_FILE_PATH, PORT)
    sys.exit(0 if success else 1)