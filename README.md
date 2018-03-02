# Podcasts Downloader

Download all new podcast episodes, which were publish since the last time. The podcast need to available by RSS.

# How this works

Give the script place for placed mp3 (a path to directory). On every run the script will check last downloaded file and RSS feed to download all new episodes.

# The list of implemented podcasts

* [The Skeptics Guide to the Universe](http://www.theskepticsguide.org/)
* [Niezatapialni](http://www.niezatapialni.pl/)
* [Squanch](https://www.stitcher.com/podcast/wisecrack-inc/the-squanch-wisecracks-rick-morty-podcast)
* [Show Me The Meaning!](https://www.stitcher.com/podcast/wisecrack-inc/show-me-the-meaning-a-wisecrack-movie-podcast)

# Using

You can use code like this one:

```python
#!/usr/bin/python
from logger import PrintingOnOut
from runner import Runner

logger = PrintingOnOut()
builder = Runner(logger)

runner = Runner(logger)
runner.add('SGTTU', '/place-where-you-store-SGTTU')
runner.add('Niezatapialni', '/place-where-you-store-Niezatapialni')
runner.add('Squanch', '/place-where-you-store-Squanch')
runner.add('SMTM', '/place-where-you-store-SMTM')
runner.run()
```