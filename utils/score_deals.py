from datetime import datetime
import re

def score_and_select_top(posts, top_n=5):
    """Score and select the top deals based on various criteria."""
    
    def score(post):
        """Calculate a score for a post based on various factors."""
        score = 0
        
        # Content-based scoring
        content = post.content.lower()
        if '75% off' in content or '75% discount' in content:
            score += 3
        if 'lifetime' in content:
            score += 2
        if 'limited time' in content or 'limited offer' in content:
            score += 1
            
        # Extract discount percentage using regex
        discount_match = re.search(r'(\d+)% (?:off|discount)', content)
        if discount_match:
            discount = int(discount_match.group(1))
            score += min(discount // 25, 3)  # Up to 3 points for high discounts
            
        # Tag-based scoring
        tags = post.get('tags', [])
        if 'AI' in tags:
            score += 1
        if 'lifetime' in tags:
            score += 1
        if 'limited' in tags:
            score += 1
            
        # Recency scoring
        date = post.get('date')
        if date:
            try:
                post_date = datetime.strptime(date, "%Y-%m-%d")
                delta = (datetime.now() - post_date).days
                score += max(0, 7 - delta)  # More points for recent posts
            except ValueError:
                pass
                
        return score
    
    # Score and sort all posts
    scored_posts = [(post, score(post)) for post in posts]
    scored_posts.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N posts
    return [post for post, _ in scored_posts[:top_n]] 