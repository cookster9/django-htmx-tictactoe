from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tictactoe_app.models import Game
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic.list import ListView
from django.db import transaction

from tictactoe_app.utilities.GameOO import GameOO


@require_http_methods(['GET','POST'])
def startGame(request):
    if request.method == "GET":
        # Handle GET request
        return render(request, "tictactoe_app/start.html", {})
    elif request.method == "POST":
        # Handle POST request
        new_game = Game.objects.create()
        new_game.save()
        return redirect('playGame', pk=new_game.id)
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Unsupported HTTP method", status=405)


@require_GET
def getWinner(request, pk):
    gameFromDB = get_object_or_404(Game, pk=pk)
    winner = gameFromDB.winner
    html = ''
    print(winner)
    if(winner==1):
        html="""<p>Player 1 wins!!</p>"""
    elif(winner==2):
        html="""<p>Player 2 wins!!</p>"""
    elif(winner==3):
        html="""<p>It's a tie!</p>"""
    else:
        html="""<p>You broke the game</p>"""
    return HttpResponse(html)


@require_http_methods(['GET','POST'])
def playGame(request, pk):
    if not request.session.session_key:
        request.session.create()
    user_id = request.session.session_key  # Unique identifier for the session
    gameFromDB = get_object_or_404(Game, pk=pk)
    locked = False
    with transaction.atomic():
        # Lock the row with SELECT ... FOR UPDATE
        locked_record = Game.objects.select_for_update().get(id=pk)

        # Check if the record is already locked
        if locked_record.locked_by == user_id or locked_record.locked_by is None:
            # Lock the record for the current user
            locked_record.locked_by = user_id
            locked_record.save()
            locked = True
    board_ary = gameFromDB.board_ary
    board_list = board_ary.split(',')
    game = GameOO(board=board_list,playerTurn=gameFromDB.player_turn,winner=gameFromDB.winner)
    if request.method == "GET":
        # Handle GET request
        #simply return game state
        winMessage = None
        if(game.winner is not None):
            if(game.winner ==1):
                winMessage = 'Player 1 wins!'
            elif(game.winner ==2):
                winMessage = 'Player 2 wins!'
            elif(game.winner ==3):
                winMessage = 'It''s a tie!'
            else:
                winMessage = 'Game is broken!'
        context = {"board": board_list, "id": gameFromDB.id, "player_turn": str(game.playerTurn)
                   ,"winner_message": winMessage,"locked": str(locked)}
        return render(request, "tictactoe_app/ttt.html", context)
    elif request.method == "POST":
        if locked == True:
            # try to make the move
            square = int(request.POST.get('coord'))
            game.makeMove(square=square)
            gameFromDB.winner = game.winner
            gameFromDB.board_ary=",".join(game.board)
            gameFromDB.player_turn=game.playerTurn
            gameFromDB.save()
            # http_response = "<div hx-swap-oob='outerHTML:#player-p'><p id='player-p'>"+str(game.playerTurn)+"</p></div>"+game.board[square]
            http_response = """<div hx-swap-oob="outerHTML:#player-p">
                                <p id="player-p">Player turn: """+str(game.playerTurn)+"""</p>
                                </div>"""+game.board[square]
            
            response_obj=HttpResponse(http_response, content_type="text/html")
            if(game.winner is not None):
                response_obj.headers['Hx-Trigger']='winnerFound'
        else:
            response_obj=HttpResponse('', content_type="text/html") # do nothing
        return response_obj
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Unsupported HTTP method", status=405)


class GameListView(ListView):
    model = Game
    # paginate_by = 50  # if pagination is desired
    ordering = ['-id']
    template_name = 'tictactoe_app/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context