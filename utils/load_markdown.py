import frontmatter
import glob
import os

def load_posts(base_path):
    """Load all markdown posts from the specified directory."""
    files = glob.glob(f"{base_path}/**/*.md", recursive=True)
    posts = []
    
    for path in files:
        try:
            post = frontmatter.load(path)
            # Add the file path to the post metadata
            post['path'] = path
            posts.append(post)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    
    return posts 