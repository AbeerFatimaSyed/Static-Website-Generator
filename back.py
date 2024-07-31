import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'generated_website'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_website():
    data = request.json
    features = data['features']

    # Set up LangChain and GROQ API
    api_key = os.getenv('GROQ_API_KEY', 'your groq api key')
    chat = ChatGroq(api_key=api_key)

    # Define the system and user messages
    system_message = "You are a helpful assistant."
    user_message = f"""
    Generate a static website with the following features:

    {features}

    Please generate the code for the website and separate files for each component. Clearly label each file with '### filename.ext' followed by the file content. If directories are needed, include them in the path like 'directory/filename.ext'. Only provide the code, no additional instructions or explanations. Make sure the code is valid and complete.
    """

    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([("system", system_message), ("human", user_message)])

    # Create the chain with the prompt and the chat model
    chain = prompt | chat

    try:
        # Generate content using the LLM
        response = chain.invoke({"text": user_message})
        generated_content = response.content

        # Validate if the generated content contains the expected file delimiters
        if "###" not in generated_content:
            return jsonify({"success": False, "error": "The generated content does not contain the expected file delimiters (###)."})

        # Set up output directory
        output_dir = app.config['UPLOAD_FOLDER']
        os.makedirs(output_dir, exist_ok=True)

        # Split generated content into files
        files = generated_content.split("###")
        result_files = {}
        for file in files:
            if "\n" in file:
                file_name, file_content = file.split("\n", 1)
                file_path = os.path.join(output_dir, file_name.strip())

                # Create directories if they don't exist
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                with open(file_path, "w") as f:
                    f.write(file_content.strip())

                result_files[file_name.strip()] = file_name.strip()  # Just the filename for the frontend

        return jsonify({"success": True, "files": result_files})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/generated_website/<path:filename>')
def serve_generated_website(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)



    
    
'''import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'generated_website'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_website():
    data = request.json
    features = data['features']

    # Set up LangChain and GROQ API
    api_key = os.getenv('GROQ_API_KEY', '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')
    chat = ChatGroq(api_key=api_key)

    # Define the system and user messages
    system_message = "You are a helpful assistant."
    user_message = f"""
    Generate a static website with the following features:

    {features}

    Please generate the code for the website and separate files for each component. Clearly label each file with '### filename.ext' followed by the file content. If directories are needed, include them in the path like 'directory/filename.ext'. Only provide the code, no additional instructions or explanations. Make sure the code is valid and complete.
    """

    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([("system", system_message), ("human", user_message)])

    # Create the chain with the prompt and the chat model
    chain = prompt | chat

    try:
        # Generate content using the LLM
        response = chain.invoke({"text": user_message})
        generated_content = response.content

        # Validate if the generated content contains the expected file delimiters
        if "###" not in generated_content:
            return jsonify({"success": False, "error": "The generated content does not contain the expected file delimiters (###)."})

        # Set up output directory
        output_dir = app.config['UPLOAD_FOLDER']
        os.makedirs(output_dir, exist_ok=True)

        # Split generated content into files
        files = generated_content.split("###")
        result_files = {}
        for file in files:
            if "\n" in file:
                file_name, file_content = file.split("\n", 1)
                file_path = os.path.join(output_dir, file_name.strip())

                # Create directories if they don't exist
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                with open(file_path, "w") as f:
                    f.write(file_content.strip())

                result_files[file_name.strip()] = file_name.strip()  # Just the filename for the frontend

        return jsonify({"success": True, "files": result_files})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/generated_website/<path:filename>')
def serve_generated_website(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)'''





