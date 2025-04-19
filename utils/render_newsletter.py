from jinja2 import Template
import datetime

def render_html(deals):
    """Render the newsletter HTML using the template."""
    with open("templates/base.html") as f:
        tmpl = Template(f.read())
    
    # Add current year for the footer
    context = {
        'deals': deals,
        'now': datetime.datetime.now()
    }
    
    return tmpl.render(**context) 