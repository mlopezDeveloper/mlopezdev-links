import reflex as rx
import link_bio_mlopez.style.styles as styles
from link_bio_mlopez.style.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style= styles.BUTTON_TITLE_STYLE),
                    rx.text(body, style= styles.BUTTON_BODY_STYLE),
                    align_items="start",
                    spacing="1",
                    padding_y= Size.SMALL.value,
                    padding_right = Size.SMALL.value
                ),
                width="100%",
                align="center"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
    