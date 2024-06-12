import reflex as rx
import link_bio_mlopez.style.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        #size = "5",
        padding_top ="24px",
        style=styles.TITLE_STYLE
    )