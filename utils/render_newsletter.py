from jinja2 import Environment, FileSystemLoader
from markdown import markdown
import datetime
import re

def clean_markdown(text):
    # Remove extra newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove markdown headers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    return text

def render_html(deals):
    # Convert markdown content to HTML with custom styling
    for deal in deals:
        # Clean the markdown first
        clean_content = clean_markdown(deal.content)
        
        # Convert to HTML with extensions
        html_content = markdown(
            clean_content,
            extensions=[
                'fenced_code',
                'tables',
                'attr_list',
                'def_list',
                'footnotes',
                'md_in_html',
                'toc'
            ]
        )
        
        # Add custom styling to the HTML
        html_content = html_content.replace('<ul>', '<ul style="list-style-type: none; padding-left: 0;">')
        html_content = html_content.replace('<li>', '<li style="margin-bottom: 10px; padding-left: 1.5em; position: relative;">')
        html_content = html_content.replace('<h2>', '<h2 style="color: var(--primary-color); margin-top: 20px;">')
        html_content = html_content.replace('<h3>', '<h3 style="color: var(--secondary-color); margin-top: 15px;">')
        html_content = html_content.replace('<strong>', '<strong style="color: var(--primary-color);">')
        
        deal['content'] = html_content

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html')
    
    return template.render(deals=deals, now=datetime.datetime.now()) 