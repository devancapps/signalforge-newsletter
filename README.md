# SignalForge Newsletter Automation

A Python-based newsletter automation system that generates and sends weekly deal digests based on markdown content from the SignalForge site.

## Features

- Automatically loads and processes markdown posts from `signalforge-site/posts`
- Scores deals based on multiple criteria:
  - Discount percentage
  - Lifetime deals
  - AI-related content
  - Post recency
  - Tags
- Renders clean, responsive HTML newsletters
- Optional email delivery via SMTP
- Weekly automated generation via GitHub Actions
- Manual trigger support for testing

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/signalforge-newsletter.git
   cd signalforge-newsletter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and configure your settings:
   ```bash
   cp .env.example .env
   ```

4. Edit `.env` with your email settings and preferences

## Usage

### Manual Generation

To generate a newsletter manually:

```bash
python generate_newsletter.py
```

This will:
1. Load posts from `../signalforge-site/posts`
2. Score and select the top deals
3. Generate HTML output in `output/`
4. Send email if configured

### Automated Generation

The newsletter is automatically generated every Friday at 12:00 UTC via GitHub Actions. You can also trigger it manually from the Actions tab in your GitHub repository.

## Directory Structure

```
signalforge-newsletter/
├── .github/workflows/generate_newsletter.yml
├── data/
│   └── featured.json                # Stores top deals (generated weekly)
├── output/
│   └── newsletter-YYYY-MM-DD.html  # Final HTML output
├── templates/
│   └── base.html                   # Jinja2 email template
├── utils/
│   ├── load_markdown.py
│   ├── score_deals.py
│   └── render_newsletter.py
├── requirements.txt
├── generate_newsletter.py
├── README.md
└── .env.example
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details 