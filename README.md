# Podcasts Downloader

Download all new podcast episodes, which were publish since the last time. The podcast need to available by RSS.

# How this works

Give the script place for placed mp3 (a path to directory). On every run the script will check last downloaded file and RSS feed to download all new episodes.

# The list of implemented podcasts

* [The Skeptics Guide to the Universe](http://www.theskepticsguide.org/)
* [Niezatapialni](http://www.niezatapialni.pl/)
* [Squanch](http://podbay.fm/show/1267014091)

# Using

You can use code like this one:

```python
#!/usr/bin/python
from logger import PrintingOnOut
from sgtu import SGTTU
from squanch import Squanch

logger = PrintingOnOut()

sgttu = SGTTU(logger, '/place-where-you-store-SGTTU')
sgttu.run()

niezatapialni = Niezatapialni(logger, '/place-where-you-store-Niezatapialni')
niezatapialni.run()

squanch = Squanch(logger, '/place-where-you-store-Squanch')
squanch.run()
```
