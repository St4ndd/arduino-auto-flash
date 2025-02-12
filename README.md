# Arduino Leonardo Auto Flash

A script for automatically updating the firmware on an Arduino Leonardo.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a script that automatically updates the firmware on an Arduino Leonardo. It identifies the device's COM port, performs a reset, and uploads the new firmware using AVRDUDE.

## Prerequisites

- Windows operating system
- [AVRDUDE](https://github.com/mariusgreuel/avrdude) installed and available in the system path
- Arduino Leonardo connected

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/St4ndd/arduino-leonardo-auto-flash.git
   ```

2. Navigate to the directory:

   ```bash
   cd arduino-leonardo-auto-flash
   ```

3. Ensure that `AVRDUDE` is installed and the path is included in the environment variable `PATH`.

## Usage

1. Place the firmware file to be flashed (`firmware.hex`) in the project directory.

2. Run the `upload.bat` script:

   ```bash
   upload.bat
   ```

   The script will automatically identify the COM port of the Arduino Leonardo, perform a reset, and upload the firmware.

## Contributing

Contributions are welcome! Please open an issue to report bugs or suggest new features.

## License

This project is licensed under the [MIT License](LICENSE).

