import reflex as rx
from link_bio_mlopez.components.link_button import link_button
from link_bio_mlopez.components.title import title
from link_bio_mlopez.style.styles import Size as Size
import link_bio_mlopez.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Transmisiones sobre programación los dias miercoles, viernes y sabados a las 22:00 ARG",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        # link_button(
        #     "Youtube",
        #     "Tutoriales sobre desarrollo de software semanales",
        #     "icons/kick.svg",
        #     const.YOUTUBE_URL
        # ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "icons/discord.svg",
            const.DISCORD_URL
        ),

        title("Recursos y más"),
        link_button(
            "Portafolio",
            "Mi sitio web",
            "icons/portafolio.svg",
            const.PORTAFOLIO_URL
        ),
        link_button(
            "Gist",
            "Code extra",
            "icons/code.svg",
            const.GIST_GITHUB
        ),
        link_button(
            "Invítame un café",
            "¿Quires ayudarme a crear contenido?",
            "icons/cafe.svg",
            const.COFEE_URL
        ),
        # link_button(
        #     "Instagram",
        #     "Red Social",
        #     "icons/kick.svg",
        #     const.INSTAGRAM_URL
        # ),

        #title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        # link_button(
        #     "Whatsapp",
        #     "Celular",
        #     "icons/kick.svg",
        #     const.WHATSAPP
        # ),
        width="100%",
        spacing="2"
    )