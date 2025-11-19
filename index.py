import solara
from components.header import Header
from components.footer import Footer

ROLE_LABELS = [
    ("Who am I?", "/my_profile"),
    ("AI Social Media Manager", "/social_media_manager"),
    ("AI Content Creator", "/content_creator"),
    ("AI Job Assistant", "/job_assistant_tracker"),
    ("AI Business Marketer", "/business_marketer"),
    ("Personal Projects", "/personal_projects"),
    ("Commercial Products", "/commercial_products"),
    ("My Calendar", "/my_calendar"),
#     ("Blog: AI/Trends/Research", "/blog_ai_trends"),
#     ("Blog: Finance & Crypto", "/blog_finance_crypto"),
]

@solara.component
def Page():
    router = solara.use_router()
    authenticated, set_authenticated = solara.use_state(False)
    show_login, set_show_login = solara.use_state(False)

    def handle_button_click(route):
        if authenticated:
            router.push(route)
        else:
            set_show_login(True)

    with solara.Column(style={
        "height": "100vh",
        "width": "100vw",
        "background": "#23272f",  # Deemed dark background
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "space-between",
        "alignItems": "stretch",
        "margin": "0",
        "padding": "0",
        "overflow": "hidden",
    }):
        Header()
        with solara.Div(style={
            "flex": "1 1 auto",
            "display": "grid",
            "gridTemplateColumns": "repeat(4, 1fr)",
            "gridTemplateRows": "repeat(2, 1fr)",
            "gap": "2.5vw",
            "width": "80vw",
            "height": "100%",
            "margin": "0",
            "padding": "2vw",
            "boxSizing": "border-box",
            "background": "#23272f",  # Match main background
        }):
            for label, route in ROLE_LABELS:
                with solara.Div(style={
                    "width": "100%",
                    "height": "100%",
                    "background": "#2d323c",
                    "borderRadius": "24px",
                    "border": "2.5px solid #444950",
                    "boxShadow": "0 4px 16px rgba(20,20,30,0.18)",
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "boxSizing": "border-box",
                    "padding": "0",
                }):
                    solara.Button(
                        label=label,
                        style={
                            "width": "90%",
                            "height": "80%",
                            "fontSize": "1.3rem",
                            "fontWeight": "bold",
                            "borderRadius": "18px",
                            "border": "none",
                            "background": "#444950",
                            "color": "#e0e6ed",
                            "boxShadow": "none",
                            "transition": "box-shadow 0.2s, border 0.2s",
                            "cursor": "pointer",
                            "whiteSpace": "normal",
                            "textAlign": "center",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "boxSizing": "border-box",
                        },
                        on_click=lambda r=route: handle_button_click(r)
                    )
        if show_login:
            with solara.Card(style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100vw",
                "height": "100vh",
                "zIndex": 1000,
                "background": "rgba(20,20,30,0.65)",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
            }):
                with solara.Column(style={
                    "background": "#23272f",
                    "padding": "2rem 2.5rem",
                    "borderRadius": "18px",
                    "boxShadow": "0 8px 32px rgba(20,20,30,0.28)",
                    "minWidth": "320px",
                    "alignItems": "center",
                }):
                    solara.Markdown("**Please log in or sign up to continue**")
                    solara.Button("Log in (demo)", color="primary", style={"background": "#2d323c", "color": "#e0e6ed"}, on_click=lambda: (set_authenticated(True), set_show_login(False)))
                    solara.Button("Cancel", color="secondary", style={"background": "#444950", "color": "#e0e6ed"}, on_click=lambda: set_show_login(False))
        Footer()

    # Expandable Chatbot Floating Button (bottom right)
    chatbot_open, set_chatbot_open = solara.use_state(False)
    with solara.Div(style={
        "position": "fixed",
        "bottom": "2.5rem",
        "right": "2.5rem",
        "zIndex": 2000,
    }):
        if chatbot_open:
            with solara.Card(style={
                "width": "340px",
                "height": "420px",
                "background": "#afb3bb",
                "color": "#e0e6ed",
                "boxShadow": "0 4px 24px rgba(20,20,30,0.28)",
                "borderRadius": "18px",
                "border": "1px solid #e0e6ed",
                "padding": "1rem",
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "flex-start",
                "position": "relative",
            }):
                with solara.Row(justify="end", style={"width": "100%", "marginBottom": "-0.5rem"}):
                    solara.Button("", icon_name="mdi-close", on_click=lambda: set_chatbot_open(False), style={
                        "background": "#5b5e63",
                        "color": "#e0e6ed",
                        "boxShadow": "none",
                        "minWidth": "32px",
                        "minHeight": "32px",
                        "width": "32px",
                        "height": "32px",
                        "borderRadius": "50%",
                        "fontSize": "1.3rem",
                        "position": "absolute",
                        "top": "0.3rem",
                        "right": "0.3rem",
                        "zIndex": 10,
                    })
                solara.Markdown("<div style='text-align:center; font-size:1.5rem; font-weight:700;'>AI Assistant</div>", "unsafe_html=True")
                solara.Markdown(":speech_balloon: How can I help you today?")
                # Placeholder for chat UI
                chat_message, set_chat_message = solara.use_state("")
                solara.InputText(label="Type your message...", value=chat_message, on_value=set_chat_message)

        else:
            solara.Button("Chat", on_click=lambda: set_chatbot_open(True), style={
                "background": "#787d88",
                "color": "#e0e6ed",
                "borderRadius": "50%",
                "width": "90px",
                "height": "64px",
                "boxShadow": "0 2px 8px rgba(20,20,30,0.18)",
                "fontSize": "1.5rem",
                "paddingLeft": "0.7rem",
                "paddingRight": "0.7rem",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
            })
