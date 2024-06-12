import reflex as rx
from link_bio_mlopez.components.link_button import link_button
from link_bio_mlopez.components.title import title
from link_bio_mlopez.style.styles import Size as Size
import link_bio_mlopez.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Kick",
            "Transmisiones sobre programación de lunes a viernes",
            "icons/kick.svg",
            const.KICK_URL
        ),
        link_button(
            "Youtube",
            "Tutoriales sobre desarrollo de software semanales",
            "icons/kick.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "icons/kick.svg",
            const.DISCORD_URL
        ),

        title("Recursos y más..."),
        link_button(
            "Portafolio",
            "Sitio personal",
            "icons/kick.svg",
            const.PORTAFOLIO_URL
        ),
        link_button(
            "LinkedIn",
            "Red laboral",
            "icons/kick.svg",
            const.LINKEDIN_URL
        ),
        link_button(
            "Github",
            "Repositorio",
            "icons/kick.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Instagram",
            "Red Social",
            "icons/kick.svg",
            const.INSTAGRAM_URL
        ),

        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "icons/kick.svg",
            f"mailto:{const.EMAIL}"
        ),
        link_button(
            "Whatsapp",
            "Celular",
            "icons/kick.svg",
            const.WHATSAPP
        ),
        width="100%",
        spacing="2"
    )