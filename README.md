## Raspberry Pi Image Capture and FTP Upload

This Python script captures an image from a Raspberry Pi camera every 10 seconds and uploads it to a remote FTP server. 

### Prerequisites

- Raspberry Pi with a camera module installed
- Python 3.x installed on the Raspberry Pi
- `picamera` and `ftplib` Python libraries installed on the Raspberry Pi
- FTP server access credentials (FTP server address, username, and password)

### Usage

1. Clone or download the repository to your Raspberry Pi.

2. Open the `capture_and_upload.py` file in a text editor.

3. Replace the following placeholders with your FTP server access credentials:

    - `your_ftp_server_address`
    - `ftp_username`
    - `ftp_password`

4. Save and close the `capture_and_upload.py` file.

5. Open a terminal window on the Raspberry Pi and navigate to the directory containing the `capture_and_upload.py` file.

6. Run the script using the following command:

    ```
    python3 capture_and_upload.py
    ```

7. The script will start capturing images from the Raspberry Pi camera and uploading them to the remote FTP server every 10 seconds. To stop the script, press Ctrl+C in the terminal.

### Error Handling

The script includes error handling to catch and print any exceptions that might occur during image capture or upload. If an error occurs, the script will print an error message and wait for 10 seconds before retrying the image capture and upload.

Note that you may need to adjust the error handling logic depending on the specific errors that you encounter while running this script.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
