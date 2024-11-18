from django.shortcuts import render, redirect
from django.http import HttpResponse
from tictactoe_app.models import Game

from tictactoe_app.utilities.GameOO import GameOO


def startGame(request):
    if request.method == "GET":
        # Handle GET request
        return HttpResponse("This is a GET request")
    elif request.method == "POST":
        # Handle POST request
        new_game = Game.objects.create()
        new_game.save()
        return redirect('playGame', pk=new_game.id) 
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Unsupported HTTP method", status=405)


def playGame(request, pk):
    try:
        gameFromDB = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse("Could not find game.")
    board_ary = gameFromDB.board_ary
    board_list = board_ary.split(',')
    game = GameOO(board=board_list,playerTurn=gameFromDB.player_turn)
    if request.method == "GET":
        # Handle GET request
        #simply return game
        return HttpResponse("This is a GET request")
    elif request.method == "POST":
        # try to make the move
        square = request.POST.get('value')
        game.makeMove(square=square)
        return HttpResponse("This is a POST request")
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Unsupported HTTP method", status=405)
