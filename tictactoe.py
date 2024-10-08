def ConstBoard(board): # to display current status of board
  print("current state of the board:\n\n ");
  for i in range(9):
    if((i>0) and (i%3==0)):
      print("\n");   #to print it in next line after every 3 values
    if(board[i]==0):      #0 in prgrm s/m  represent empty spaces in game by user
      print("_ ",end=" ");  #end is a predefined parameter for getting space between the elements there
    if(board[i]==-1):     # -1 in s/m represent X in game
      print("X",end=" ");
    if(board[i]==1):     #1 in s/m represent O in game by user
      print("O",end=" ");
  print("\n \n");


def User1Turn(board):
  pos=input("\n \n Enter X's pos[1-9]  ");
  pos=int(pos);
  if(board[pos-1]!=0):   #bcoz user gives index from 1 but s/m counts frm 0 therefr do pos-1 or index-1
    print("Wrong Move !!");
    exit(0);
  board[pos-1]=-1;


def User2Turn(board):
  pos=input("\n \n Enter O's pos[1-9]  ");
  pos=int(pos)
  if(board[pos-1]!=0):   #bcoz user gives index from 1 but s/m counts frm 0 therefr do pos-1 or index-1
    print("Wrong Move !!");
    exit(0);
  board[pos-1]=1 ;  #to represent O by 1 in s/m



def analyseboard(board): #checking someone has won or not
   cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
   for i in range(8):
     if(board[cb[i][0]]!=0 and board[cb[i][0]]==board[cb[i][1]] and board[cb[i][0]]==board[cb[i][2]]):
       return board[cb[i][0]] ;   #value of the one who won
     
   return 0;    #indicates no one has won



def minmax(board,player): # here player is passed bcoz we need to know whose chance it is currently
    x=analyseboard(board);
    if(x!=0): # i.e.someone has won
      return (x*player);
    pos = -1;
    value = -2; # to compare values with the 0,-1,1 to get max among them so we need a lesser value than all of these to compare so -2
    for i in range(9):
     if(board[i]==0):
      board[i]=player;
      score=-minmax(board,player*-1); 
      board[i]=0;
      if(score>value):
       value=score;
       pos=i;
      if(pos==-1): # i.e. not able to find a position to place i/p value
       return 0;
    return value;


def CompTurn(board):
   pos =-1; 
   value= -2; # to compare values with the 0,-1,1 to get max among them so we need a lesser value than all of these to compare so -2
   for i in range(9):
    if(board[i]==0):
      board[i]=1; # bcoz computer player value is 1 here
      score=-minmax(board, -1); #
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
   board[pos]=1;


def main():
  choice=input("enter 1 for single player, 2 for multiplayer:");
  choice=int(choice);
  board=[0,0,0,0,0,0,0,0,0];
  if(choice==1):
    print("Computer: O  Vs. You: X");
    player =input("enter to play first(1) or second(2):");
    player=int(player);
    for i in range(0,9):   # loop from 0 to less than 9 i.e. till 8 bcoz exact 9 times input can be/is taken . this loop checks before each i/p that : 1]whethr someone won, or 2]its player 1 chance or 3]player 2 chance
      if(analyseboard(board)!=0):  # analyse func. checks whther someone won/its a draw match in that board which has those inputs list
        break;
      if((i+player)%2==0):     # to check whose chance it is, ie. if ==0 then its AIs turn,else human's
        CompTurn(board);
      else:
        ConstBoard(board); # shows/displays current status of the board
        User1Turn(board);

  else:   #if choice==2
    for i in range(0,9):   # loop from 0 to less than 9 i.e. till 8 bcoz exact 9 times input can be/is taken . this loop checks before each i/p that : 1]whethr someone won, or 2]its player 1 chance or 3]player 2 chance
      if(analyseboard(board)!=0):  #analyse func. checks whther someone won/its a draw match in that board which has those inputs list
         break;
      if(i%2==0):     # to check whose chance it is, ie. if ==0 then its AIs turn,else human's
          ConstBoard(board);
          User1Turn(board);
      else:
          ConstBoard(board);
          User2Turn(board);

  x=analyseboard(board); # to get and store the final result of the analyse board
  if(x==0):
         ConstBoard(board);
         print("Draw !");
  if(x==-1):
         ConstBoard(board);
         print("Player X wins !!! O looses");  #bcoz -1 represent x and 1 is 0 here by us
  if(x==1):
         ConstBoard(board);
         print("Player O wins !!! X looses");
