# Static Website Generator

This project is a static website generator built using Flask and LangChain with the GROQ API. It allows users to input features for their desired website and generates the corresponding static website files.

## Features

- **User Input for Features**: Users can specify the features they want in their website through a text area.
- **Automated Code Generation**: Utilizes LangChain and GROQ API to generate static website code based on user input.
- **Download and Preview**: Generated website files can be downloaded individually, and there is an option to preview the generated website.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- LangChain
- GROQ API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/static-website-generator.git
   cd static-website-generator

2. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your GROQ API key in the `config.py` file:
    ```python
    apikey = "your_groq_api_key"
    ```

## Usage

1. Run the Flask application:
    ```bash
    python back.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

3. Enter the desired features for your website and click "Generate Website". The generated files will be available for download and preview.

## Project Structure
``` bash
static-website-generator/
│
├── templates/
│ └── index.html
│
├── static/
│ └── styles.css
│
├── generated_website/
│ └── [Generated website files will be stored here]
│
├── .gitignore
├── README.md
├── back.py
├── config.py
└── requirements.txt
```
 
