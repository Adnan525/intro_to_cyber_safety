# Social Media Metadata Analysis

## Overview

This demonstration aligns with our lecture material on social media security and privacy. According to the lecture, we need to be careful when sharing data on social media. However, social media companies do make efforts to protect user privacy in ways users might not realise. This demo will show how platforms like Facebook strip potentially sensitive metadata from photos to protect users.

## Requirements

- Linux environment (Ubuntu or Kali)
- Two image files:
  - An original photo taken directly from a smartphone/camera
  - The same photo after being uploaded to and downloaded from Facebook
- ExifTool installed

## Setup Instructions

1. Install [ExifTool](https://exiftool.org/) if not already available:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libimage-exiftool-perl
   ```

2. Create a directory for the demo:
   ```bash
   mkdir ~/metadata_demo
   cd ~/metadata_demo
   ```

3. Copy your original photo and Facebook-downloaded photo to this directory

## Running the Demo

1. Analyze the original photo:
   ```bash
   exiftool original_photo.jpg
   ```

2. Analyze the Facebook-downloaded photo:
   ```bash
   exiftool facebook_photo.jpg
   ```

3. Compare the metadata found in both photos to show what Facebook has stripped:
   ```bash
   # For a cleaner comparison of just GPS data
   echo "Original GPS data:"
   exiftool -T -GPSLatitude -GPSLongitude original_photo.jpg
   
   echo "Facebook photo GPS data:"
   exiftool -T -GPSLatitude -GPSLongitude facebook_photo.jpg
   
   # For device info comparison
   echo "Original device information:"
   exiftool -T -Make -Model -CreateDate original_photo.jpg
   
   echo "Facebook photo device information:"
   exiftool -T -Make -Model -CreateDate facebook_photo.jpg
   ```

4. GPS coordinates can be checked using Goole Earth like `34° 24' 8.76" N, 132° 27' 32.52" E` or, convert to decimal format `34.4024, 132.4590` to use in Google Maps

## Key Points to Emphasize

1. **Meta-Protection:** Facebook and many platforms strip sensitive metadata like GPS coordinates, protecting users even if they don't realize it's happening

2. **Original Files Still Risky:** Original photos on your device contain full metadata and sharing these directly (via email, messaging, etc.) exposes this data

3. **The "Deleted But Not Gone" Principle:** Even when Facebook strips visible metadata, they may retain this information on their servers for their own purposes

4. **Personal Responsibility:** Users should still be cautious and aware of metadata in their original files

## Alternative Demonstration Methods

### Online EXIF Viewer
For a more visual approach, try using an online EXIF viewer:
1. Go to https://exif.tools/ or https://exifdata.com
2. Upload both the original and Facebook photos
3. Compare the metadata side-by-side

<!-- ### Method 2: Image Steganography Demo
To expand the demonstration to show how images can contain hidden data:
1. Install Steghide: `sudo apt-get install steghide`
2. Hide a text file in an image: `steghide embed -cf image.jpg -ef secret.txt`
3. Extract the hidden file: `steghide extract -sf image.jpg`
4. This demonstrates that images can contain more information than is visible -->

<!-- ### Method 3: Metadata Command-Line Tools Comparison
Compare results from multiple tools to show consistency:
```bash
# Install tools
sudo apt-get install exiftool exiv2 imagemagick

# Compare outputs
exiftool image.jpg
exiv2 image.jpg
identify -verbose image.jpg
``` -->

## Conclusion

1. Metadata in digital images can reveal significant private information
2. Social media platforms implement privacy protections by stripping sensitive metadata
3. Original files still contain this sensitive data
4. Users must be aware of what information they're potentially sharing
5. The principle that "even when deleted, it may not be deleted" applies to digital content in various contexts