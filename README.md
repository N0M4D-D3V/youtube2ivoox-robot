<div align="center">
  <a href="https://github.com/N0M4D-D3V/youtube2ivoox-robot">
    <img style="width:350px; text-align:center; border: 5px black solid; border-radius: 20%;background-color: white;" src="icon.webp" alt="application logo">
  </a>

<h3 align="center" style="font-size:3rem">Youtube2ivooX</h3>
  <p align="center">
    Python automation agent for upload podcast to ivoox from youtube. This script works with english ivoox/youtube pages only.
  </p>
</div>

## BUILD IN

- Python 3
- Selenium
- macOS

## START

1. **Open a Terminal or Command Prompt**

2. **Navigate to Your Project Directory**: Use the cd command to change to the directory where you want to create the virtual environment.

3. **Create a Virtual Environment**: Run the following command to create a new virtual environment. You can name it anything you like, but venv is a common choice.

   ```zsh
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```zsh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```zsh
     source venv/bin/activate
     ```
5. **Install Requirements**: Once the virtual environment is activated, you can install the packages listed in **requirements.txt** file by running:
   ```zsh
   pip install -r requirements.txt
   ```
6. **Verify Installation**: You can check if the packages were installed correctly by listing the installed packages:

   ```zsh
   pip list
   ```

7. **Run**: To run the script, ensure you configured the **setup.py**. Then, run this command:
   ```zsh
   python3 main.py
   ```
