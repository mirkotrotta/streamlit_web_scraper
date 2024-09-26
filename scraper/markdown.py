from markdownify import markdownify as md

# Convert HTML to markdown
def convert_to_markdown(html_content):
    return md(html_content)

# Save the markdown content to a file
def save_to_markdown(markdown_content, output_file):
    with open(output_file, "w") as file:
        file.write(markdown_content)
    print(f"Markdown content saved to {output_file}")
