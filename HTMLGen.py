class html():
    def __init__(self,woning):
        self.woning = woning

    def genereer_html(self):
        html = "<html><head><title>Status Overzicht</title></head><body>"
        html += "\n<h1>Overzicht per kamer</h1>"
        for kamer in self.woning.kamers.lijst:
            html += f"\n<h2>{kamer.kamernaam}</h2>\n\t<ul>"
            for apparaat in kamer.apparaten:
                html += f"<li>{apparaat}</li>"
            html += "\n\t</ul>"
        html += "\n</body></html>"

        with open("HTML/status_overzicht.html", "w") as f:
            f.write(html)

