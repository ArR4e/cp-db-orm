<h1>Developer and Databeses 101</h1>

NB! If you have questions you can write to Karel Paan <code>(karelpaan#2890)</code> in Discord chat ;)

**Greetings, wanderer!** You have found yourself on a quest to get to know more about the life of a database and how it is used in "real life".
Keep in mind that this is only one of many uses for a database. Development being the most common usa we will be talking about just that. And ofcourse you will have plenty of opporunities to make your hands dirty. 

Note that this application is not ment to look "nice" or give the best user experience but only to give you an **insight into databases in development**.

Furthermore, this application uses rather old way of designing an application (<u>monolithic architecture</u>).
This is not to say it is good or bad, although nowadays using <u>microservice architecture</u> is much more common, the main thing here is that you get to know databases and get some experience using them in application development.

It is also recommended googling the underlined words ;).

<h2>Setup</h2>

FORK the repository to your local machine (if you haven't already). I do recommend the web version, but it is up to you.
<a href="https://docs.github.com/en/get-started/quickstart/fork-a-repo">HINT</a>

<h4>Install all necessary packages</h4>
```bash
$ pip install -r requirements.txt
```

To run the application you must first setup environment variables like so:
<h4>Mac</h4>
```bash
$ export FLASK_APP=application
$ export FLASK_ENV=development
```

<h4>Linux</h4>
```bash
> set FLASK_APP=application
> set FLASK_ENV=development
```

<h4>Windows</h4>
```bash
> $env:FLASK_APP = "application"
> $env:FLASK_ENV = "development"
```

<h3>Init DB</h3>
```bash
flask init-db
```
<h3>Run</h3>
```bash
flask run
```

<h2>Assignment 0</h2>

<div style="background-color: rgba(82,63,63,0.78); padding: 0.1rem 1rem; border-radius: 20px">
For your changes to work you need to rerun the project after every change, this process is mad easy by PyCharm ;).
</div>

<ul>
 <li>Read the before manual, start the application 
 (default port is 5000, if you waht to change that, use `flask run --host=0.0.0.0 --port=80`)</li>
 <li>Register an account</li>
 <li>Log in</li>
 <li>Create a post</li>
 <li>Try to edit a post (THIS SHOULDN'T WORK)</li>
</ul>

<h2>Assignment 1</h2>
Your first task is to implement SQL queries `get_post` and `update` inside application/blog.py.
Tip: Look at `index` and `create` functions respectively.
<ul>
 <li>Implement beforementioned SQL scripts</li>
 <li>Try to edit a post again, now it should be working, if not, you did something wrong!</li>
</ul>

<h2>Running tests</h2>
If all assignments are done correctly then all tests should pass.
(You can also run the tests inside PyCharm, it makes no difference.)
```bash
 python -m pytest tests
```

<h2>Assignment 2</h2>
<hr>
<h3>NB! To start Assignmet 2 checkout to branch "assignment2"!</h3>
<hr>
