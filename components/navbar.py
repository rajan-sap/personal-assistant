import solara

@solara.component
def Navbar():
    with solara.Card(style={"background": "#1a202c", "color": "#fff", "padding": "1rem", "borderRadius": "0 0 12px 12px", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"}):
        solara.Markdown("""
        <div style='display: flex; align-items: center;'>
            <img src='https://img.icons8.com/ios-filled/50/ffffff/robot-2.png' width='32' style='margin-right: 1rem;'>
            <span style='font-size: 1.5rem; font-weight: bold;'>Personal Assistant</span>
        </div>
        """)
