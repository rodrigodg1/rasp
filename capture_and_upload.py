import time
import picamera
import ftplib

# Set up camera and FTP connection
camera = picamera.PiCamera()
ftp = ftplib.FTP('your_ftp_server_address', 'ftp_username', 'ftp_password')

# Set up image capture and upload loop with error handling
while True:
    try:
        # Capture image and save to file
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'image_{timestamp}.jpg'
        camera.capture(filename)

        # Upload image to FTP server
        with open(filename, 'rb') as file:
            ftp.storbinary(f'STOR {filename}', file)

    except Exception as e:
        print(f'Error: {e}')
        # Wait for 10 seconds before retrying
        time.sleep(10)
        continue

    else:
        print(f'Uploaded {filename} to FTP server')
        # Wait for 10 seconds before capturing the next image
        time.sleep(10)

# Clean up resources
camera.close()
ftp.quit()
