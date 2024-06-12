import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .font import Font, FontWeight


#Constants
MAX_WIDTH = "560px"

#Fuentes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Raleway:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

#Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

#Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        #"display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

NAVBAR_TITLE_STYLE = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

TITLE_STYLE = dict(
    width="100%",
    size = "5",
    paddding_top=Size.DEFAULT.value
)

BUTTON_TITLE_STYLE = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size= Size.DEFAULT.value,
    color= TextColor.HEADER.value
)

BUTTON_BODY_STYLE = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size= Size.MEDIUM.value,
    color= TextColor.BODY.value
)

