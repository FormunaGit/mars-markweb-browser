from textual.app import App, on
from textual.widgets import Footer, Header, Input, Markdown
from textual.containers import ScrollableContainer
import requests

class css:
    CSS = """
    .hidden {
        display: none;
    }
    """

class MarsBrowser(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("s", "toggle_search", "Toggle Search Bar"),
    ]

    CSS = css.CSS
    def on_input_submitted(self, event):
        pageraw = requests.get(f"https://ivo-markweb-server.vercel.app/page/{event.value}").text
        page = Markdown(pageraw)
        self.query_one("#searchbar").add_class("hidden")
        self.mount(page)


    def compose(self):
        yield Header()
        #-------------------
        yield Input(placeholder="Input link here...", id="searchbar")
        #-------------------
        yield Footer()
    
    def action_toggle_search(self):
        self.query_one("#searchbar").toggle_class("hidden")

if __name__ == "__main__":
    MarsBrowser().run()