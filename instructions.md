# W4 - API's PROJECT - TODO's

- A) Choose a dataset you like from `kaggle.com`.
  
- B) Create a python script and name it `main.py`. Requirements for this script:
  - `main.py` must not have more than 100 lines.
    - Separate code into other `.py` files. Create functions or classes if needed.
  - It must receive at least **4 params** via command-line flags `--param1` `--param2`.
    - Use `argparse` for this task.
    - Those parameters should be used to filter the dataset.
  
- C) Filter the dataset with the params received from `main.py`
  - Note: You can clean the dateset beforehand in another script/notebook or do it directly in the `main.py` execution
  
- D) Enrich the dataset with external data, you have to choose at least one of the following:
  - L1) Get data from an API.
  - L2) Use an API that requires authentication via token or oAuth.
  - L3) Do basic web scraping with python `requests` module.
  - L4) Perform advanced web scraping with `selenium`.
  
- E) Create some reports containing valuable data from the dataset. You have to choose at least one of the following:
  - L1) Simply sumarize the data and do some basic statistics \(`mean`, `max`, `min`, `std`, etc.).
  - L2) Do domain based statistics or data aggregations using `groupby()` .
  - L3) Create two different plots based on your input command line arguments
  
- F) Export the report, you have to choose at least one of the following.
  - L1) Simple text report that will be printed in console `stdout` using `print()`.
  - L2) Create a PDF file `report.pdf` with your text report and plots.
  - L3) Send a mail using python `smtplib` library to someone. Add a `--mailto` flag in your `main.py` and include a text report inside the mail.
  - L4) 🚧HARD MODE:🚧 Mail with PDF file attatched and plots inside pdf file.
  
- **G**) **NEW SEASON THIS BOOTCAMP** Advanced Mailing techniques
  - L1) 🚴🏻‍♂️ Generate a HTML email with embedded images & visual report
  - L2) 🚀 Use a mail sending service `API`. `Sengrid` Free plan allows 40k emails/day with it's free plan.
- **E**) 🔥AMAZING🔥 Get an automatic `Slack` message every time someone opens an email with your report.🤷🏼‍♂️ Use the slack api for this.

## How to deliver the project

Create a new repo with the name `apis-project` in your github account. Open an `ISSUE` with the link to your repo

## Links & Resources

- <https://docs.python.org/3/library/argparse.html>
- <https://github.com/n0shake/Public-APIs>
- <https://docs.python.org/3/library/smtplib.html>
- <https://realpython.com/python-send-email/>
- <https://2.python-requests.org/en/master/>
- <https://github.com/theskumar/python-dotenv>
- <https://selenium-python.readthedocs.io>
- <https://selenium-python.readthedocs.io/getting-started.html#example-explained>
- <https://pyfpdf.readthedocs.io/en/latest/>
- <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>

## Prolinks

- <https://sendgrid.com/pricing/>
- <https://www.socketlabs.com/developers/>
