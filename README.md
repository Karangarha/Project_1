# CPS-3500 Project
**Quick tip:** *click on the green play button to run the code* 
## Download the git file
- Open the designation location and run Terminal
- Run command <br> `git clone https://github.com/Karangarha/Project_1.git`

## Install the requirement

> - Create new [conda](https://anaconda.org/anaconda/conda) environment <br>`conda create --name my-env -y`
> - Activate conda environment  <br> `conda activate my-env`
> - Install the required python libraries <br> `pip install -r requirements.txt`
>



## Initialize Database
### * Note : The file does not include database
> Run the following commands to initialize the migration in python IDE
>```bash  
>flask db init
>```
>```bash
>flask db migrate -m "initial migration" 
>```
>```bash
>flask db upgrade 
>```
>This will create a migration folder

> The following command create a database
> 
>` python query.py `
> 
> This will create instance folder including the database from faker

## Test the Application
>Run ` pytest ` in terminal to check that there is no error
>```bash 
>pytest
>```

## Run the main application to view web pages
>
>`python wsgi.py`<br>
>
> The program will show the following on terminal
>```commandline
>C:\Users\Work\.conda\envs\Project_1\python.exe wsgi.py 
> * Serving Flask app 'application'
> * Debug mode: off
> WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
> * Running on all addresses (0.0.0.0)
> * Running on http://127.0.0.1:5000
> * Running on http://10.0.0.235:5000
> Press CTRL+C to quit
> ```
> Press `CTRL` and click on `http link` a browser window will pop-up <br>
> Now you can navigate between webpages<br>
> 
> **Tip: On users webpage click any `<username>` to check there profile**