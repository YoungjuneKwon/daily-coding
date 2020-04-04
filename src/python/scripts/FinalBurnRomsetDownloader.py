def requests_get(url):
  import requests
  return requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

def extract_links(url):
  from bs4 import BeautifulSoup
  return [e.attrs['href'] for e in BeautifulSoup(requests_get(url).content).select('.imageblock a')]

def download(download_root, url):
  import requests
  r = requests_get(url)
  filename = r.headers['Content-Disposition'].split('=')[-1].replace('"', '')
  with open(f'{download_root}/{filename}', 'wb') as f:
    f.write(r.content)

def main():
  import itertools
  prefix = 'https://dsno.tistory.com/'
  pages = '582 583 584 585 586 587 588 589 590'.split()
  urls = list(itertools.chain(*[extract_links(f'{prefix}{p}') for p in pages]))
  [download('./fbdown', u) for u in urls]

if __name__ == '__main__':
  main()