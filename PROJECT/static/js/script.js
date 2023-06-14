$(document).ready(function() {
    $(".dots").click(function() {
      $(".options, h2").css("visibility", "hidden");
      $(".title").css("visibility", "hidden");
      $("td").css("visibility", "visible");
      aiCo = "#f22853";
      huCo = "#108cff";
    });
    $(".dots2").click(function() {
      $(".options, h2").css("visibility", "hidden");
      $(".title").css("visibility", "hidden");
      $("td").css("visibility", "visible");
    });
  
    $("td").click(function() {
      move(this, huPlayer, huCo);
      console.log("clicked");
    });
  });
  var board = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  var huPlayer = "P";
  var aiPlayer = "C";
  var iter = 0;
  var round = 0;
  var aiCo = "#108cff";
  var huCo = "#f22853";
  
  function move(element, player, color) {
    console.log("element"+ element.id);
    if (board[element.id] != "P" && board[element.id] != "C") {
      round++;
      $(element).css("background-color", color);
      board[element.id] = player;
      console.log(board);
  
      if (winning(board, player)) {
        setTimeout(function() {
          alert("YOU WIN");
          reset();
        }, 500);
        return;
      } else if (round > 8) {
        setTimeout(function() {
          alert("TIE");
          reset();
        }, 500);
        return;
      } else {
        round++;
        var index = minimax(board, aiPlayer).index;
        var selector = "#" + index;
        $(selector).css("background-color", aiCo);
        // $(selector).css("border-radius", "10px");
        board[index] = aiPlayer;
        console.log(board);
        console.log(index);
        if (winning(board, aiPlayer)) {
          setTimeout(function() {
            alert("YOU LOSE");
            reset();
          }, 500);
          return;
        } else if (round === 0) {
          setTimeout(function() {
            alert("tie");
            reset();
          }, 500);
          return;
        }
      }
    }
  }
  
  function reset() {
    round = 0;
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    $("td").css("background-color", "transparent");
  }
  
  function minimax(reboard, player) {
    iter++;
    let array = avail(reboard);
    if (winning(reboard, huPlayer)) {
      return {
        score: -10
      };
    } else if (winning(reboard, aiPlayer)) {
      return {
        score: 10
      };
    } else if (array.length === 0) {
      return {
        score: 0
      };
    }
  
    var moves = [];
    for (var i = 0; i < array.length; i++) {
      var move = {};
      move.index = reboard[array[i]];
      reboard[array[i]] = player;
  
      if (player == aiPlayer) {
        var g = minimax(reboard, huPlayer);
        move.score = g.score;
      } else {
        var g = minimax(reboard, aiPlayer);
        move.score = g.score;
      }
      reboard[array[i]] = move.index;
      moves.push(move);
    }
  
    var bestMove;
    if (player === aiPlayer) {
      var bestScore = -10000;
      for (var i = 0; i < moves.length; i++) {
        if (moves[i].score > bestScore) {
          bestScore = moves[i].score;
          bestMove = i;
        }
      }
    } else {
      var bestScore = 10000;
      for (var i = 0; i < moves.length; i++) {
        if (moves[i].score < bestScore) {
          bestScore = moves[i].score;
          bestMove = i;
        }
      }
    }
    return moves[bestMove];
  }
  
  //available spots
  function avail(reboard) {
    return reboard.filter(s => s != "P" && s != "C");
  }
  
  // winning combinations
  function winning(board, player) {
    if (
      (board[0] == player && board[1] == player && board[2] == player) ||
      (board[3] == player && board[4] == player && board[5] == player) ||
      (board[6] == player && board[7] == player && board[8] == player) ||
      (board[0] == player && board[3] == player && board[6] == player) ||
      (board[1] == player && board[4] == player && board[7] == player) ||
      (board[2] == player && board[5] == player && board[8] == player) ||
      (board[0] == player && board[4] == player && board[8] == player) ||
      (board[2] == player && board[4] == player && board[6] == player)
    ) {
      return true;
    } else {
      return false;
    }
  }