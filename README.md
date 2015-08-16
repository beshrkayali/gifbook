# Gif Book
Create sequenced Gifs from video clips and subtitles.


## Prerequisites

Make sure that you have ImageMagick and GhostScript installed:

```bash
$ brew install ImageMagick
$ brew install gs
```

## Installation

```bash
$ pip install gifbook
```

## Using `gifbook` as a command line tool

```bash
$ gifbook Night.Of.The.Living.Dead.1968.mkv Night.Of.The.Living.Dead.1968.srt --compression 50 --resize 30
```

More options are available, you can check them out by typing:

```bash
$ gifbook --help
```

## Using `gifbook` as a module


```python
from gb import GifBook

gb = GifBook('Night.Of.The.Living.Dead.1968.720p.mkv', '~/Desktop/gifs/')

gb.set_subtitles(
    "Night.Of.The.Living.Dead.1968.720p.srt",
)

gb.generate(resize=0.5, compression=30)
```

## Demo Gifs

![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_50.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_51.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_52.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_53.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_54.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_55.gif)



## License
License under [GNU GPL](http://www.gnu.org/licenses/gpl.txt)

![GNU GPL LOGO](http://www.gnu.org/graphics/gplv3-127x51.png)





