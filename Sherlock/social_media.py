# social_media_finder/social_media.py
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

# Initialize the rich console
console = Console()

# Updated platforms and URL patterns
platforms = {
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter (X)": "https://www.twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/user/{}",
    "WhatsApp": "https://www.whatsapp.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://www.tumblr.com/blog/{}",
    "Discord": "https://www.discord.com/{}",
    "Telegram": "https://t.me/{}",
    "WeChat": "https://www.wechat.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Viber": "https://www.viber.com/{}",
    "Medium": "https://medium.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Myspace": "https://myspace.com/{}",
    "Periscope": "https://www.pscp.tv/{}",
    "Foursquare": "https://foursquare.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Clubhouse": "https://www.clubhouse.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://www.dribbble.com/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "BitChute": "https://www.bitchute.com/channel/{}",
    "VKontakte (VK)": "https://vk.com/{}",
    "TikTok Lite": "https://www.tiktoklite.com/@{}",
    "Sina Weibo": "https://weibo.com/{}",
    "Gab": "https://gab.com/{}",
    "Parler": "https://parler.com/profile/{}",
    "Rumble": "https://rumble.com/c/{}",
    "Locals": "https://locals.com/profile/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "Odysee": "https://odysee.com/@{}",
    "BitClout (DeSo)": "https://bitclout.com/u/{}",
    "Steemit": "https://steemit.com/@{}",
    "Minds": "https://www.minds.com/{}",
    "Bebo": "https://www.bebo.com/{}",
    "Ello": "https://www.ello.co/{}",
    "Mix": "https://www.mix.com/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "MeWe": "https://mewe.com/i/{}",
    "Nextdoor": "https://nextdoor.com/profile/{}",
    "Line": "https://line.me/ti/p/{}",
    "KakaoTalk": "https://www.kakaocorp.com/service/KakaoTalk/{}",
    "Baidu Tieba": "https://tieba.baidu.com/home/main?id={}",
    "Qzone": "https://qzone.qq.com/{}",
    "Douban": "https://www.douban.com/people/{}",
    "Renren": "https://www.renren.com/{}",
    "Mixi": "https://mixi.jp/show_friend.pl?id={}",
    "YouNow": "https://www.younow.com/{}",
    "Funimate": "https://www.funimate.com/u/{}",
    "Lomotif": "https://www.lomotif.com/u/{}",
    "Triller": "https://triller.co/@{}",
    "We Heart It": "https://weheartit.com/{}/collections",
    "Flipboard": "https://www.flipboard.com/@{}",
    "Flipagram": "https://www.flipagram.com/{}",
    "Socialcam": "https://www.socialcam.com/{}",
    "Plurk": "https://www.plurk.com/{}",
    "Taringa": "https://www.taringa.net/{}",
    "Peeks Social": "https://www.peeks.social/{}",
    "Skyrock": "https://www.skyrock.com/members/{}/profile",
    "Tagged": "https://www.tagged.com/{}",
    "Viadeo": "https://www.viadeo.com/p/{}",
    "LiveJournal": "https://www.livejournal.com/profile/{}",
    "Friendster": "https://www.friendster.com/{}",
    "GIPHY": "https://giphy.com/channel/{}",
    "Amino": "https://aminoapps.com/u/{}",
    "Houseparty": "https://www.houseparty.com/@{}",
    "Yubo": "https://www.yubo.live/u/{}",
    "Path": "https://www.path.com/{}",
    "Signal": "https://www.signal.org/{}",
    "Whisper": "https://whisper.sh/u/{}",
    "Kik": "https://www.kik.com/u/{}",
    "VSCO": "https://vsco.co/{}",
    "Peach": "https://www.peach.cool/@{}",
    "Digg": "https://digg.com/u/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "CafeMom": "https://www.cafemom.com/profile/{}",
    "Fotolog": "https://www.fotolog.com/{}",
    "Koo": "https://www.kooapp.com/profile/{}",
    "Hive Social": "https://www.hivesocial.app/u/{}",
    "Polywork": "https://www.polywork.com/{}",
    "Fishbrain": "https://www.fishbrain.com/u/{}",
    "Gas": "https://www.gasapp.co/u/{}",
    "Peanut": "https://www.peanut-app.io/u/{}",
    "Swarm": "https://www.swarmapp.com/u/{}",
    "Untappd": "https://www.untappd.com/user/{}",
    "Club Penguin Rewritten": "https://www.cprewritten.net/user/{}",
}

def check_url(platform, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            console.print(f"[+] [bold green]{platform}[/bold green]: Found at {url}")
            return url
        else:
            console.print(f"[-] [bold red]{platform}[/bold red]: Not found", style="dim")
    except KeyboardInterrupt:
        console.print(f"[^] [bold red] KeyboardInterrupted by user")
        exit()        
    except Exception as e:
        console.print(f"[!] Error checking {platform}: {e}", style="bold red")

def find_social_media(username):
    table = Table(title="Social Media Search Results", show_header=True, header_style="bold blue")
    table.add_column("Platform", justify="left", style="bold")
    table.add_column("Status", justify="center")
    table.add_column("URL", justify="right")
    
    for platform, url_pattern in platforms.items():
        try:
           url = url_pattern.format(username)
           status = "Found" if check_url(platform, url) else "Not Found"
           table.add_row(platform, status, url)
        except KeyboardInterrupt:
            console.print(f"[^] [bold red] KeyboardInterrupted by user")
            exit() 
           
    
    console.print(table)
