from pptx import Presentation


def gradientsetter(fill, angle, stop1, stop2):
    fill.gradient()
    fill.gradient_angle = angle
    fill.gradient_stops[0].color.rgb = stop1
    fill.gradient_stops[1].color.rgb = stop2
    return fill