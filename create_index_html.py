def create_index_html():
    # HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Research Website</title>
</head>
<body>
    <h1>Welcome to My Research Website</h1>
    <p>This is a placeholder text. You can replace it with your own content.</p>
</body>
</html>
"""

    # Write HTML content to index.html file
    with open("index.html", "w") as file:
        file.write(html_content)
    
    print("index.html file created successfully.")

if __name__ == "__main__":
    create_index_html()
