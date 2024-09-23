FLASK-RESUME
    
## Usage

To generate a PDF version of your resume, follow these steps:

1. Make sure you have Python 3 installed on your system.

2. Run the `main.py` file using the following command:
  
   ```shell
    python3 main.py
    ```


3. Install the required dependencies by running the following command in your terminal:

    ```shell
    pip install pdfkit
    ```

4. Open the `main.py` file and add the following code at the end:

    ```python
    import pdfkit

    pdfkit.from_url('http://127.0.0.1:5000/', 'pooja_resume.pdf', options={'disable-smart-shrinking': '', 'dpi': 400, 'print-media-type': True, 'margin-left': '5', 'margin-top': '10', 'margin-right': '1', 'margin-bottom': '3', 'page-height': '255', 'page-width': '210'})
    ```

5. Save the file and exit.

6. In your terminal, navigate to the project directory:

    ```shell
    cd /Users/poojanshetty/Documents/Personal_projects/flask-resume/
    ```

7. After the Flask server starts, open your web browser and visit `http://127.0.0.1:5000/`.

8. Once the page loads, the PDF version of your resume will be automatically generated and saved as `pooja_resume.pdf` in the project directory.

That's it! You have successfully generated a PDF version of your resume using Flask-Resume.
pdfkit.from_url('http://127.0.0.1:5000/', 'pooja_resume.pdf', options={'disable-smart-shrinking': '','dpi': 400, 'print-media-type': True,'margin-left': '10mm','margin-top': '10mm', 'margin-right': '10mm', 'margin-bottom': '10mm', 'page-size': 'A4'})



pdfkit.from_url('http://127.0.0.1:5000/', 'pooja_resume.pdf', options={'disable-smart-shrinking': '','dpi': 400,'print-media-type': True,'margin-left': '5mm','margin-top': '5mm','margin-right': '5mm','margin-bottom': '5mm','page-size': 'A4'})