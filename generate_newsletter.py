from utils.load_markdown import load_posts
from utils.score_deals import score_and_select_top
from utils.render_newsletter import render_html
import os
import datetime

def main():
    # Load and process posts
    posts = load_posts("../signalforge-site/posts")
    ranked = score_and_select_top(posts)

    # Render HTML
    html = render_html(ranked)

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Write to output
    out_file = f"output/newsletter-{datetime.date.today()}.html"
    with open(out_file, 'w') as f:
        f.write(html)

    # Create latest.html for preview
    with open("output/latest.html", 'w') as f:
        f.write(html)

    # Send email if configured
    if os.getenv("SEND_EMAIL") == 'true':
        from utils.send_email import send
        send(html)

if __name__ == "__main__":
    main() 