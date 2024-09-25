from .social_media import find_social_media
from .banner import print_banner

if __name__ == "__main__":
    print_banner()
    try:
       username = input("Enter the username: ")
       find_social_media(username)
    except KeyboardInterrupt:
        exit()
        
