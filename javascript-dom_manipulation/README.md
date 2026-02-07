# JavaScript - DOM Manipulation

This project contains exercises demonstrating fundamental DOM (Document Object Model) manipulation techniques using vanilla JavaScript.

## Description

This project is part of the Holberton School curriculum focusing on JavaScript and DOM manipulation. It covers essential concepts for interacting with HTML elements programmatically, including selecting elements, modifying styles, handling events, and making API requests.

## Learning Objectives

By completing this project, you will understand:

- How to select HTML elements in JavaScript
- How to manipulate CSS styles using JavaScript
- How to work with CSS classes
- How to handle DOM events
- How to make API requests using `fetch`
- How to manipulate and update the DOM dynamically

## Files

| File | Description |
|------|-------------|
| `0-script.js` | Updates the text color of the `<header>` element to red (#FF0000) |
| `1-script.js` | Updates the text color of the `<header>` element to red when the user clicks on the tag with id `red_header` |
| `2-script.js` | Adds the class `red` to the `<header>` element when the user clicks on the tag with id `red_header` |
| `3-script.js` | Toggles the class of the `<header>` element between `red` and `green` when the user clicks on the tag with id `toggle_header` |
| `4-script.js` | Adds a `<li>` element to a list when the user clicks on the tag with id `add_item` |
| `5-script.js` | Removes all `<li>` elements from a list when the user clicks on the tag with id `clear_list` |
| `6-script.js` | Fetches the character name from an API and displays it in the tag with id `character` |
| `7-script.js` | Fetches and lists all movie titles from an API in the tag with id `list_movies` |
| `8-script.js` | Fetches and displays a translation of "Hello" depending on the language from an API |

## Requirements

- All files are interpreted on Chrome (version 57.0 or later)
- All files end with a new line
- Code is semistandard compliant with semicolons on top
- Not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data

## Usage

Each script is designed to work with corresponding HTML files. To use:

1. Include the script in your HTML file before the closing `</body>` tag
2. Ensure required HTML elements (with specific IDs) are present
3. Open the HTML file in a web browser

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DOM Manipulation</title>
</head>
<body>
    <header>Header</header>
    <div id="red_header">Click me</div>
    <script type="text/javascript" src="1-script.js"></script>
</body>
</html>
```

## Author

iid7oomii - Holberton School