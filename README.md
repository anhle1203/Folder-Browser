# Project Browser (Instruction for Windows Users)

This project is built upon my VP's request to support the Business Intelligence department to search for previous analysis more efficiently. The team is carrying an average of 65 analsysis projects concurrently, not to mention 

## For First-Time Users

### Steps to Set Up and Run the Project

1. **Install & Configure pip:**
   - Go to [Python Downloads](https://www.python.org/downloads/windows/) and install the latest version of Python for Windows.
![alt text](Screenshots\image1.png)
   - During installation, choose ONLY the option “Add python.exe to PATH” and proceed with the installation.
![alt text](Screenshots\image2.png)

2. **Install Required Libraries and Run Using Command Prompt (Terminal):**
![alt text](Screenshots\image3.png)
   - Open Command Prompt and create a virtual path to the network path:
     ```bash
     pushd /your/root/folder/path/here
     ```
   - View files/folders in the current directory:
     ```bash
     dir
     ```
![alt text](Screenshots\image4.png)
   - Install required libraries to run the program:
     ```bash
     pip install -r requirements.txt
     ```
     **Note:** It may take a while for the first time. Notice the line “Successfully installed” which means all libraries are installed.
![alt text](Screenshots\image5.png)

3. **Run the Program:**
   - Run `RetrieveData.py` to update `metadata.txt` database:
     ```bash
     python retrieveData.py
     ```
     **Note:** The code is done after it creates a line to process new commands.
![alt text](Screenshots\image6.png)
   - Run `mainCode.py` to show the interface and perform the search:
     ```bash
     python mainCode.py
     ```
     **Note:** After running the script, it takes 10-15 seconds to pop up a screen. This is where the project will take your keyword input and return the most related folders fetched from the database.
![alt text](Screenshots\image7.png)
4. **Close the Terminal After Using:**
   - To close the virtual path:
     ```bash
     popd
     ```

## For Return Users

### 1st Option: Faster but Needs a Little Technical Knowledge (5-8s to Work)

- Run the commands listed in the “Run the Program” step in the "For First-Time Users" section.

### 2nd Option: Less Technical but Takes More Time (15-30s to Work)

- Go to the “Project Browser” folder and double-click `retrieveData.py` and `mainCode.py`.

## FAQs & Useful Commands

1. Update pip to the latest version:
   ```bash
   python -m pip install --upgrade pip
2. Check if python/pip is installed
   ```bash
   python --version
   pip --version

    ** If pip or Python is not found, click back to the “python-3.12.4-amd64” file you installed and choose “Uninstall” + make sure that reinstall with the right option I mentioned above. You need python.exe in the PATH to make the program work

3. Clear the terminal interface
    ```bash
    cls
