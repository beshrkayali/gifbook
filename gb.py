#!/usr/bin/env python
"""
GifBook: Create sequenced Gifs from video clips and subtitles
"""

__author__ = "Beshr Kayali"
__copyright__ = "Copyright 2015, The Gif Church Project"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "me@beshr.com"
__status__ = "Prototype"


import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


class GifBook(object):
    def __init__(self, clip, output_dir):
        super(GifBook, self).__init__()
        self._clip_file = clip
        self._clip = VideoFileClip(clip)
        self._output_dir = output_dir

    def generate(self,
                 start_sub=None, end_sub=None, resize=.5, compression=20):
        subs = pysrt.open(self._subtitles_file)

        for iter_, sub in enumerate(subs, start_sub if start_sub else 0):
            if end_sub and iter_ > end_sub:
                break

            gif_file_name = '{dir}/{clip}_{iter}.gif'.format(
                dir=self._output_dir,
                clip=self._clip_file,
                iter=iter_
            )

            clip = (
                self._clip
                .subclip((sub.start.minutes, sub.start.seconds),
                         (sub.end.minutes, sub.end.seconds))
                .resize(resize)
            )

            compositions = [clip]

            subtitles_y_pos = self._subtitles_position_y
            for line in sub.text.split('\n'):
                subtitles_y_pos += 20

                text = (
                    TextClip(line,
                             fontsize=self.subtitles_font_size,
                             color=self.subtitles_color,
                             stroke_width=self.subtitles_stroke_width,
                             stroke_color=self.subtitles_stroke_color,
                             bg_color=self.subtitles_background_color,
                             font=self.subtitles_font_name)

                    .set_pos((self._subtitles_position_x,
                              subtitles_y_pos))

                    .set_duration(clip.duration))

                compositions.append(text)

            composition = CompositeVideoClip(compositions)

            composition.write_gif(gif_file_name, fuzz=compression)

    def set_subtitles(self, subtitles_file, subtitles_config=None):
        self._subtitles_file = subtitles_file

        if subtitles_config is None:
            subtitles_config = {}

        # Defaults
        self._subtitles_font_size = subtitles_config.get(
            'font_size', 18)

        self._subtitles_color = subtitles_config.get(
            'color', 'white')

        self._subtitles_background_color = subtitles_config.get(
            'bg_color', 'black')

        self._subtitles_font_name = subtitles_config.get(
            'font_name', 'Times-Roman')

        self._subtitles_stroke_width = subtitles_config.get(
            'stroke_width', 0)

        self._subtitles_stroke_color = subtitles_config.get(
            'stroke_color', 'black')

        self._subtitles_position_x = subtitles_config.get(
            'position_x', 20)

        self._subtitles_position_y = subtitles_config.get(
            'position_y', 200)

    @property
    def subtitles_font_size(self):
        return self._subtitles_font_size

    @property
    def subtitles_font_name(self):
        return self._subtitles_font_name

    @property
    def subtitles_color(self):
        return self._subtitles_color

    @property
    def subtitles_background_color(self):
        return self._subtitles_background_color

    @property
    def subtitles_stroke_width(self):
        return self._subtitles_stroke_width

    @property
    def subtitles_stroke_color(self):
        return self._subtitles_stroke_color

    @property
    def subtitles_position_x(self):
        return self._subtitles_position_x

    @property
    def subtitles_position_y(self):
        return self._subtitles_position_y
