# Accio Notes (Jekyll Blog)

This repository hosts a Jekyll-based, blogger-style site deployed with GitHub Pages.

## Local development

1. Install Ruby and Bundler.
2. Install dependencies:
   gem install bundler jekyll
3. Run the site locally:
   jekyll serve
4. Open http://localhost:4000/github_notes

## Adding a new post

- Create a file in `_posts` named `YYYY-MM-DD-title.md` with front matter:
  ---
  layout: post
  title: Your Post Title
  tags: [tag1, tag2]
  ---

## GitHub Pages

- Ensure repository is configured to build GitHub Pages from the default branch.
- The site uses the `minima` theme and safe plugins (`jekyll-feed`, `jekyll-seo-tag`).

## Structure

- `_layouts/default.html` — base layout
- `_layouts/post.html` — single post layout
- `_posts/` — blog posts
- `index.html` — home page list of posts
- `_pages/about.md` — about page"# notes" 


this is the notes file

live at https://harmeet773.github.io/notes/
