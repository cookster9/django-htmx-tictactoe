Years ago I flubbed an interview question that asked me to implement tictactoe in object oriented programming. Fast forward to now, I wanted to practice HTMX, so I figured I could take another crack at tictactoe and might as well make the game logic in an object oriented way to redeem myself. Along the way I found Tailwind CSS and took this chance to try that out too.

Useful scripts:

Start tailwind watcher, which generates css as you add classes to html:
tailwindcss -i ./tictactoe_app/static/tictactoe_app/input.css -o ./tictactoe_app/static/tictactoe_app/output.css --watch

Prune tailwind output, which takes out anything you aren't using:
