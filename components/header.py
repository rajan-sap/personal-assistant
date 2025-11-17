import solara

@solara.component
def Header():
    solara.Markdown("""
    <div style='font-size:2.2rem; font-weight:700; color:gray; margin-bottom:1.2rem;'>👋 Personal Assistant</div>
    """)