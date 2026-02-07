# Python - Server Side Rendering

## Description
This project explores server-side rendering (SSR) using Python Flask and Jinja2 templating. It demonstrates how to dynamically generate HTML content on the server before sending it to the client, including template rendering, dynamic data display, file handling, and database integration.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the concept of server-side rendering and its benefits
- Use Flask framework to create web applications
- Implement Jinja2 templates with dynamic content
- Work with template inheritance and template includes
- Handle data from multiple sources (JSON, CSV, SQLite)
- Implement conditional rendering and loops in templates
- Render data dynamically from various data sources

## Requirements
- Python 3.x
- Flask
- Jinja2
- SQLite3 (for database tasks)

## Project Structure
```
python-server_side_rendering/
├── README.md
├── task_00_intro.py           # Template string generation
├── task_01_jinja.py           # Basic Flask routes with Jinja2
├── task_02_logic.py           # Jinja2 with conditional logic
├── task_03_files.py           # Reading from JSON and CSV files
├── task_04_db.py              # Database integration with SQLite
├── templates/
│   ├── index.html             # Home page template
│   ├── about.html             # About page template
│   ├── contact.html           # Contact page template
│   ├── items.html             # Items list with conditional rendering
│   ├── product_display.html   # Product display with tables
│   ├── header.html            # Reusable header component
│   └── footer.html            # Reusable footer component
├── items.json                 # Sample JSON data
├── products.json              # Products data in JSON format
├── products.csv               # Products data in CSV format
└── products.db                # SQLite database file
```

## Tasks

### Task 0: Introduction to Template Generation
**File:** `task_00_intro.py`

Generate personalized invitation files from a template string and attendee data.
- Implements input validation for template and attendees
- Replaces placeholders with actual values or "N/A" if missing
- Generates numbered output files (output_1.txt, output_2.txt, etc.)

**Usage:**
```python
from task_00_intro import generate_invitations

template = "Hello {name}, you are invited to {event_title} on {event_date} at {event_location}."
attendees = [
    {"name": "Alice", "event_title": "Conference", "event_date": "2024-03-15", "event_location": "NYC"},
    {"name": "Bob", "event_title": "Workshop", "event_date": "2024-04-20", "event_location": "SF"}
]
generate_invitations(template, attendees)
```

### Task 1: Basic Jinja2 Templates
**File:** `task_01_jinja.py`

Create a Flask application with basic routes and Jinja2 templates:
- `/` - Home page
- `/about` - About page
- `/contact` - Contact page

Templates include reusable header and footer components.

**Run:**
```bash
python task_01_jinja.py
```
Visit: `http://localhost:5000`

### Task 2: Jinja2 with Conditional Logic
**File:** `task_02_logic.py`

Extends the previous task to include dynamic data rendering:
- `/items` route displays items from `items.json`
- Implements conditional rendering (shows "No items found" if list is empty)
- Uses Jinja2 loops to iterate through items

### Task 3: Reading Data from Files
**File:** `task_03_files.py`

Dynamic product display from JSON or CSV files:
- `/products?source=json` - Read from `products.json`
- `/products?source=csv` - Read from `products.csv`
- `/products?source=json&id=1` - Filter by product ID
- Error handling for missing files and invalid sources
- Displays products in an HTML table

**Features:**
- Supports both JSON and CSV data sources
- Optional filtering by product ID
- Comprehensive error handling

### Task 4: Database Integration
**File:** `task_04_db.py`

Extends Task 3 to include SQLite database support:
- `/products?source=sql` - Read from SQLite database
- `/products?source=json` - Read from JSON file
- `/products?source=csv` - Read from CSV file
- All features from Task 3 plus database querying

**Database Schema:**
```sql
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iid7oomii/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-server_side_rendering
```

2. Install required packages:
```bash
pip install flask
```

3. Run any task:
```bash
python task_01_jinja.py
# or
python task_02_logic.py
# or
python task_03_files.py
# or
python task_04_db.py
```

## Testing

### Test Task 1, 2, 3, or 4:
1. Start the Flask application
2. Open your browser and navigate to:
   - `http://localhost:5000/` - Home page
   - `http://localhost:5000/about` - About page
   - `http://localhost:5000/contact` - Contact page
   - `http://localhost:5000/items` - Items list (Task 2+)
   - `http://localhost:5000/products?source=json` - Products from JSON (Task 3+)
   - `http://localhost:5000/products?source=csv` - Products from CSV (Task 3+)
   - `http://localhost:5000/products?source=sql` - Products from database (Task 4)

### Test Task 0:
```python
python3
>>> from task_00_intro import generate_invitations
>>> # Test with your data
```

## Key Concepts

### Server-Side Rendering (SSR)
SSR involves generating HTML on the server before sending it to the client, providing:
- Better SEO (search engine optimization)
- Faster initial page load
- Better performance on low-powered devices

### Jinja2 Templating
- **Variables:** `{{ variable }}`
- **Conditionals:** `{% if condition %}...{% endif %}`
- **Loops:** `{% for item in items %}...{% endfor %}`
- **Template Inheritance:** `{% include 'template.html' %}`

## Author
- **iid7oomii** - [GitHub Profile](https://github.com/iid7oomii)

## Repository
**GitHub:** [holbertonschool-higher_level_programming](https://github.com/iid7oomii/holbertonschool-higher_level_programming)

**Directory:** `python-server_side_rendering`

## License
This project is part of the Holberton School curriculum.