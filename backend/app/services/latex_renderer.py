from jinja2 import Template
import subprocess
import uuid
import os

LATEX_TEMPLATE = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\begin{document}
{{ content }}
\end{document}
"""

def render_pdf(resume_text: str):
    resume_id = str(uuid.uuid4())
    tex_file = f"/tmp/{resume_id}.tex"
    pdf_file = f"/tmp/{resume_id}.pdf"

    template = Template(LATEX_TEMPLATE)
    tex_content = template.render(content=resume_text)

    with open(tex_file, "w") as f:
        f.write(tex_content)

    subprocess.run(["pdflatex", "-output-directory=/tmp", tex_file])

    return pdf_file, tex_file
