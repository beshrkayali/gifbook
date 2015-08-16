# Gif Book
Create sequenced Gifs from video clips and subtitles.


## Example

```python
from gb import GifBook

gb = GifBook('Night.Of.The.Living.Dead.1968.720p.mkv', '~/Desktop/gifs/')

gb.set_subtitles(
    "Night.Of.The.Living.Dead.1968.720p.srt",

    subtitles_config={
        'font_size': 26,
        'font_name': 'Helvetica',
        'stroke_width': 2.1,
        'stroke_color': 'grey',
        'position_y': 300
    }
)

gb.generate(resize=0.6)
```

## Demo Gifs

![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_0.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_1.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_2.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_3.gif)
![](../master/demo/Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.mkv_4.gif)


## Prerequisites

Make sure that you have ImageMagick and GhostScript installed:

```bash
$ brew install ImageMagick
$ brew install gs
```


## License
License under [GNU GPL](http://www.gnu.org/licenses/gpl.txt)

![GNU GPL LOGO](http://www.gnu.org/graphics/gplv3-127x51.png)





