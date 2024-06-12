import reflex as rx
import link_bio_mlopez.style.styles as styles
from link_bio_mlopez.style.styles import Size as Size
from link_bio_mlopez.style.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text("mlopez", color=Color.PRIMARY.value, style=styles.NAVBAR_TITLE_STYLE),
            rx.text("dev", color=Color.SECONDARY.value, style=styles.NAVBAR_TITLE_STYLE)
        ),
        position="sticky",#posicion que queda fija 
        bg= Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",#siempre va a estar en la parte superior de todo
        top="0"
    )


