import reflex as rx
from link_bio_mlopez.components.link_icon import link_icon
from link_bio_mlopez.components.info_text import info_text
from link_bio_mlopez.style.styles import Size as Size
from link_bio_mlopez.style.colors import TextColor as TextColor
import link_bio_mlopez.constants as const
from link_bio_mlopez.style.colors import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                size="7",
                src="avatar.jpg",
                padding ="2px",
                border_radius="100px",
                border = f"4px solid {Color.PRIMARY.value}"
                ),
            rx.vstack(
                rx.heading("MARCOS LÓPEZ"),
                rx.text(
                    "@mlopez",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "github"
                        ),
                    link_icon(
                        "icons/linkedin-in.svg",
                        const.LINKEDIN_URL,
                        "linkedIn"
                        ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "instagram"
                        ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "tiktok"
                    )
                ),
                align_items="start"
            ),
            spacing="2"
        ),
        rx.flex(
            info_text("+4","años de experiencia"),
            rx.spacer(),
            info_text("2","aplicación creada"),
            rx.spacer(),
            info_text("0","seguidores"),
            width="100%"
        ),
        rx.text(""" Soy Programador desde hace más de 4 años.  
                Actualmente trabajo como Analista IT en CNP Seguros.
                Ademas he desarrollado mis propias aplicaciones como freelance para distintos clientes.
                Aqui podrás encontrar todos mis enlaces de ínteres. !Bienvenid@¡""",
                font_size = Size.MEDIUM.value,
                color=TextColor.BODY.value
                ),
        spacing= "5",
        align_items="start"
    )