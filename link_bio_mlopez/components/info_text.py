import reflex as rx
from link_bio_mlopez.style.styles import Size as Size
from link_bio_mlopez.style.colors import Color as Color
from link_bio_mlopez.style.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.strong(title,font_weight="bold",color=Color.PRIMARY.value),
        f" {body}", font_size= Size.MEDIUM.value, color=TextColor.BODY.value
    )

#color_scheme="indigo"

#font_weight="bold", color="blue"