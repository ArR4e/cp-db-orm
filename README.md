<h1>Developer and Databeses 102 (Assignment 2)</h1>

**Greetings, wanderer!** We meet again... this time, as promised we will take a look inside world of ORMs and try it out ourselves.

NB! If you have questions you can write to Karel Paan <code>(karelpaan#2890)</code> in Discord chat ;)

<h2>Assignment 2 (The real deal)</h2>

<hr>
<div style="background-color: rgba(82,63,63,0.78); padding: 0.1rem 1rem; border-radius: 20px">

Now to the main part of this exercise... ORM ([Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)).

ORM offers us a nice way to describe our database inside our code, which also unites the database objects with the back-end objects.

ORM makes it easy to maintain models and develop fast and reliably.

The main trade-off with ORM is that it does not perform queries as fast as native SQL scripts and can it can have difficulties when implementing niche models/relations.
The latter and sometimes the first can be averted by adding custom SQL to problematic pieces.


As with all things IT, there is no clear benefit but the decision should be made considering the complexity and the required time of a certain system.

We will also implement ORM in our project, for this we use SQLAlchemy, the most popular ORM for python.

As you see, SQLAlchemy is no magic and it works perfectly together with pure SQL from our previous example (<code>auth.py</code>).
Basically it is a neat way to write SQL :D.

To understand what is going on, check <code>application/__init__.py</code>
</div>

<h3>Tasks</h3>
(Everything should be done inside <code>blog.py</code> file)
Tasks require you to search individually, you can find help in Google or in <a href="https://docs.sqlalchemy.org/en/14/">HERE</a>.
<ol>
    <li>Implement <code>get_post</code> function's SQL</li>
    <li>Implement <code>update</code> function's SQL</li>
    <li>Implement <code>search</code> function's SQL, you can test this by querying in the GUI ;)</li>
</ol>
<hr>

<div style="background-color: rgba(82,63,63,0.78); padding: 0.1rem 1rem; border-radius: 20px">

A little more info before you go, hope you liked the tasks given and decide to create your own application someday or why not <strong>today</strong>.

Keep in mind the example we used here today is not to show the best layout for a web project rather than show you the cool opportunities that databases offer.

E.g. a real application would use <u>migrations</u> and keep models in different files for better structure and readability. If you have questions, then Google it ;). 
</div>

<h2>Deliverables</h2>
The end result should pass all tests that are written for you. There is no point in fooling said tests as they are only there for your benefit!
If all is well, share the repository (GitHub) link with Karel Paan <code>(karelpaan#2890)</code> in Discord.
