import bs4 as bs
import urllib.request

# Get website link and open it
website = str(input('Enter link to your Overwatch 2 profile from overwatch.blizzard.com:\n'))
source = urllib.request.urlopen(website).read()

# Create beautifulsoup object -- source gives response data, soup is html data we can interact with
soup =bs.BeautifulSoup(source, 'lxml')

# Find Rank links (rank itself comes from an image link)
rank_urls = []
for img in soup.find_all('img', class_='Profile-playerSummary--rank'):
    rank_urls.append(img.get('src'))

# Take the links to the ranks and remove everything except for the rank name itself
clean_ranks = []
for url in rank_urls:
    clean_ranks.append(url[61:-15])

# Place into dict
ranks = {}
keys = ['tank', 'dps', 'support']

for i in range(len(keys)):
    ranks[keys[i]] = clean_ranks[i]

print(ranks)