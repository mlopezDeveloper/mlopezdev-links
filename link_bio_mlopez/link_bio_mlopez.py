import reflex as rx
from link_bio_mlopez.components.navbar import navbar
from link_bio_mlopez.components.footer import footer
from link_bio_mlopez.views.header.header import header
from link_bio_mlopez.views.links.links import links
import link_bio_mlopez.style.styles as styles
from link_bio_mlopez.style.styles import Size as Size

# class State(rx.State):
#     pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="MlopezDev | Aprendemos junto a la comunidad",
    description="Hola, mi nombre es Marcos Lopez. Soy Analista IT, desarrollador freelance",
    image="logo.ico"
    )
app._compile()
