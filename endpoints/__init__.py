from flask import render_template as raw_render_template
from htmlmin import minify


def render_template(*args, **kwargs):
    return minify(raw_render_template(*args, **kwargs), remove_comments=True, remove_empty_space=True)
