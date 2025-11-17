import solara

job_sources = [
    ("indeed", "Indeed"),
    ("linkedin", "LinkedIn"),
    ("glassdoor", "Glassdoor"),
    ("monster", "Monster"),
    ("custom", "Custom Source")
]

@solara.component
def Page():
    keywords, set_keywords = solara.use_state("")
    selected_sources, set_selected_sources = solara.use_state(["indeed", "linkedin"])
    jobs, set_jobs = solara.use_state([])
    loading, set_loading = solara.use_state(False)

