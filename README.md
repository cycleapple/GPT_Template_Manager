# GPT Templates

GPT Templates is a web application for creating and managing templates for generating text using GPT models. It allows users to create templates with prompts and prompt descriptions, and categorize them by topic. The templates can be edited, deleted, and copied to the clipboard for use in generating text. Additionally, any text within square brackets will be highlighted in blue.

## Getting Started

### Prerequisites

To run this application, you will need:

* Python 3.7 or higher
* pip

### Installing

1. Clone this repository to your local machine:

```bash
git clone https://github.com/cycleapple/gpt-templates.git
```

2. Change into the project directory:

```bash
cd gpt-templates
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Initialize the database:

```bash
python app.py db init
python app.py db migrate
python app.py db upgrade
```

### Running the application

To start the application, run:

```bash
python app.py
```

Then, open your web browser and navigate to `http://localhost:5000`.

## Usage

### Creating a template

To create a new template, click the "Create Block" button on the home page and fill in the title, prompt, prompt description, and category fields. Any text within square brackets will be highlighted in blue. Click "Create Block" to save the template.

### Editing a template

To edit an existing template, click the "Edit" button on the template card and make your changes. Click "Save" to update the template.

### Deleting a template

To delete a template, click the "Delete" button on the template card.

### Copying a prompt

To copy a prompt to the clipboard, click the "Copy" button on the template card.

### Filtering templates by category

To filter templates by category, click on the category button in the navigation bar.

## Built With

* Flask - A Python web framework
* Flask-SQLAlchemy - A Flask extension for SQLAlchemy
* Jinja - A web templating engine
* Bootstrap - A front-end framework for building responsive websites

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.