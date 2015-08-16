from gb import GifBook
import click
import os


@click.command()
@click.option('--font-name', default='Helvetica',
              help='Font name of subtitles overlayed on generated gifs.')
@click.option('--font-size', default=18,
              help='Font size of subtitles overlayed on generated gifs.')
@click.option('--font-color', default='white',
              help='Font color of subtitles overlayed on generated gifs.')
@click.option('--background-color', default='black',
              help='Background color of subtitles overlayed on generated gifs.')
@click.option('--stroke-width', default=0, type=float,
              help='Stroke width of subtitles overlayed on generated gifs.')
@click.option('--stroke-color', default='black',
              help='Stroke color of subtitles overlayed on generated gifs.')
@click.option('--x-position', default=20,
              help='X position of subtitles block')
@click.option('--y-position', default=300,
              help='Y position of subtitles block')
@click.option('--resize', default=1, type=float,
              help='Size of generated Gifs. Between 0 and 1.')
@click.option('--compression', default=0, type=float,
              help='Compression of generated gifs.')
@click.argument('video_file', type=str)
@click.argument('subtitles_file', type=str)
@click.argument('out_dir', type=str, default='gifs', required=False)
def cli(video_file,
        subtitles_file,
        out_dir,
        font_name,
        font_size,
        font_color,
        background_color,
        stroke_width,
        stroke_color,
        x_position,
        y_position,
        resize,
        compression):
    """Generates sequenced Gifs from video clips and SubRip (.srt) subtitle files"""

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    gb = GifBook(video_file, out_dir)

    gb.set_subtitles(
        subtitles_file,  # "Night.Of.The.Living.Dead.1968.720p.BRRip.x264-x0r.srt",
        subtitles_config={
            'font_name': font_name,
            'font_size': font_size,
            'font_color': font_color,
            'bg_color': background_color,
            'stroke_width': stroke_width,
            'stroke_color': stroke_color,
            'position_x': x_position,
            'position_y': y_position
        }
    )

    gb.generate(resize=resize, compression=compression)
