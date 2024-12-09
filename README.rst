============
django-tictactoe-htmx
============

Tic-tac-toe in browser, made with Django, HTMX, Tailwind. 

Years ago I flubbed an interview question that asked me to implement tictactoe in object oriented programming. 
Fast forward to now, I wanted to practice HTMX
, so I figured I could take another crack at tictactoe and might 
as well make the game logic in an object oriented way to redeem myself. 
Along the way I found Tailwind CSS and took this chance to try that out too. 
So, simply a condensed way to practice Django, HTMX, OOP in Python, and Tailwind CSS. 

Hopefully you aren't misled to believe that this is any kind of useful HTMX package.

Quick start
-----------

1. Add "tictactoe_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "tictactoe_app",
    ]

2. Include the tictactoe URLconf in your project urls.py like this::

    path("tictactoe/", include("tictactoe_app.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the ``/tictactoe/`` URL to play.