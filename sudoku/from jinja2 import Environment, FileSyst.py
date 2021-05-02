from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("index.html")
M = [[1, 2, 3], [1, 2, 3]]
template_vars = {"M" : M }
HTML(string=html_out).write_pdf("report.pdf")