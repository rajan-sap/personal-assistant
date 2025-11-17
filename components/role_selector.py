import solara

roles = [
    ("/social", "Social Media Manager"),
    ("/blog-ai", "Blog: AI/Trends/Research"),
    ("/blog-finance-crypto", "Blog: Finance & Crypto"),
    ("/blog-general", "Blog: General Affairs"),
    ("/job-finder", "Personal Job Finder"),
    ("/products", "Products"),
    ("/business", "Business"),
    ("/personal-projects", "Personal Projects")
]

@solara.component
def RoleSelector():
    current_route = solara.use_route()
    for route, label in roles:
        style = {
            "display": "block",
            "width": "100%",
            "padding": "0.7rem 1rem",
            "margin": "0.3rem 0",
            "borderRadius": "8px",
            "background": "#4a5568" if current_route == route else "#2d3748",
            "color": "#fff",
            "textDecoration": "none",
            "fontWeight": 500,
            "transition": "background 0.2s",
            "cursor": "pointer",
        }
        solara.Link(label, route, style=style)
