import reflex as rx
import datetime 
from link_bio_mlopez.style.styles import Size as Size
from link_bio_mlopez.style.colors import TextColor as TextColor
import link_bio_mlopez.constants as const

def footer() -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="logo.ico",
                        height=Size.VERY_BIG.value,
                        weight=Size.VERY_BIG.value,
                        alt="Logotipo de MLopezDev."
                    ),   width="100%"
                ),
                rx.link(
                    f"© 2019-{datetime.date.today().year} Sitio Por MLopez.",
                    href= const.PORTAFOLIO_URL,
                    is_external=True,
                    font_size=Size.MEDIUM.value,
                    width="100%",
                    text_align="center"
                ),
                rx.text(
                        " DESARROLLANDO MIS SUEÑOS DESDE ARGENTINA - BUENOS AIRES",
                        font_size=Size.MEDIUM.value,
                        margin_top=Size.ZERO.value,
                        width="100%",
                        text_align="center"
                    ),
                margin_bottom=Size.BIG.value,
                padding_bottom=Size.BIG.value,
                padding_x= Size.BIG.value,
                color=TextColor.FOOTER.value
                
            )
    )