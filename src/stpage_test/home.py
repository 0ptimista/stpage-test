from st_pages import Page, Section, show_pages

show_pages(
    [
        Page("stpage_test/home.py", "Home"),
        Section(name="Section"),
        Page("stpage_test/about.py", "About"),
    ]
)
