"""
A units converter than can convert MPG to KPL precisely to 4 decimal places
"""


def mpg2kpl(mpg):
    return round(mpg * 1.609344 * 0.2641720524, 4)
