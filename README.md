# Sherlock-Style Social Media Account Finder 
## Author : N V R K SAI KAMESH SHARMA 

A Python tool to search for usernames on multiple social media platforms. The script takes a username as input and checks across 100+ popular social media platforms to see if the username exists.


![image](https://github.com/user-attachments/assets/2dcd1fdc-6e0d-443d-a66c-83cde0a37d88)

![image](https://github.com/user-attachments/assets/5bb4221d-b134-4463-8a04-1a186c819040)



## Features
- Supports 100+ social media platforms.
- Shows if the username is found and provides a direct link.
- Uses `requests` for HTTP requests and `rich` for a beautifully formatted console output.

## Handling of Errors, Invalid Links, and Predictions
- Not all platforms may respond: Some links might produce errors or time out if the platform does not respond correctly. The script handles this by showing an error message for that platform.
- Invalid Links: Some platforms may return invalid results if the username does not exist or the platform no longer uses the URL pattern provided. In such cases, the script will notify you with a warning and move on to the next platform.
- Imperfect Predictions: The tool may attempt to search for usernames but may not always correctly predict the availability or existence of a username on some platforms. False positives or false negatives may occur due to differences in platform behavior, changes in URL structures, or inconsistent API responses.
- Working URLs: The script highlights successful matches in green, while errors or platforms that return no results are shown in red.

## Requirements

Before running the script, ensure you have installed the required dependencies by running:

```bash
git clone https://github.com/kalasaikamesh/Kala-Sherlock.git 
cd Kala-Sherlock
pip install -r requirements.txt
python -m sherlock.main

```
## if u are using wsl2 like kali etc....

```bash
git clone https://github.com/kalasaikamesh/Kala-Sherlock.git 
cd Kala-Sherlock
sudo apt install python3-pip
pip3 install -r requirements.txt
python3 -m sherlock.main
```

