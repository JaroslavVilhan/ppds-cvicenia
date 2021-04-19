import urllib.request


def download_file(url, filename):
    with urllib.request.urlopen(url) as f:
        file = f.read()
    with open(filename, "w+b") as outfile:
        outfile.write(file)


urls = [
    'https://uim.fei.stuba.sk/wp-content/uploads/2018/02/2021-07.iteracia-'
    'generator-korutina.pdf',
    'https://uim.fei.stuba.sk/wp-content/uploads/2018/02/2021-01.uvod-do'
    '-paralelnych-a-distribuovanych-vypoctov.pdf',
    'https://uim.fei.stuba.sk/wp-content/uploads/2018/02/2021-04b'
    '.diningphilosophers.pdf '
    ]

count = 0
for url in urls:
    download_file(url, 'file' + str(count) + '.pdf')
    count += 1
