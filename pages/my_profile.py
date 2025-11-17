import solara

@solara.component
def Page():
    solara.Title("My Profile")
    with solara.Column(style={
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "3rem 0",
        "minHeight": "60vh",
        "color": "#e0e6ed",
        "background": "#23272f",
        "borderRadius": "18px",
        "boxShadow": "0 4px 24px rgba(20,20,30,0.18)",
        "maxWidth": "500px",
        "margin": "2rem auto"
    }):
        solara.Markdown("""
# 👤 My Profile

Welcome to your personal profile page!

- **Name:** John Doe
- **Email:** johndoe@email.com
- **Role:** User

---

_You can customize this page to show your personal info, settings, and more._
""")
