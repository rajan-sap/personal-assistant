import solara

@solara.component
def Footer():
    solara.Markdown("""
    <div style='width:100vw; text-align:center; margin-top:2vh; color:#888; font-size:1rem;'>
        © 2025 Personal Assistant. All rights reserved.
    </div>
    """)
