import solara
from components.role_selector import RoleSelector

@solara.component
def Sidebar():
    with solara.Sidebar():
        with solara.Card(style={"background": "#2d3748", "color": "#fff", "padding": "1rem", "margin": "1rem 0", "borderRadius": "12px"}):
            solara.Markdown("""
            <div style='font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>Roles</div>
            """)
            RoleSelector()
