from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from tictactoe_app.models import Game
from django.utils.html import format_html

from tictactoe_app.utilities.GameOO import GameOO


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


def playGame(request, pk):
    gameFromDB = get_object_or_404(Game, pk=pk)
    board_ary = gameFromDB.board_ary
    board_list = board_ary.split(',')
    game = GameOO(board=board_list,playerTurn=gameFromDB.player_turn,winner=gameFromDB.winner)
    if request.method == "GET":
        # Handle GET request
        #simply return game state
        context = {"board": board_list, "id": str(gameFromDB.id), "player_turn": str(game.playerTurn)}
        return render(request, "tictactoe_app/ttt.html", context)
    elif request.method == "POST":
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
        return HttpResponse(http_response, content_type="text/html")
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Unsupported HTTP method", status=405)
