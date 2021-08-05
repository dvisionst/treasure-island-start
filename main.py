print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
           / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
         /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input(f'You'"'"'re at a crossroad, which way do you want to go?\nType "left" or "right"?\n')



if direction == "left":
  print("You choose the right path. You're safe.")
  lake = input('You come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n')
  if lake == "wait":
    print("You wait for the boat and make it safely across the lake.")
    doors = input('You come across three different colored doors along the wall.\nType "red" to open the red door.\nType "yellow" to open the yellow door.\nType "blue" to open the blue door.\n')
    if doors == "yellow":
      print("CONGRATS! You have found the tresure door.\nYou Win!!!")
    elif doors == "red":
      print("You open the red door to a raging fire. You are burned alive and die.\nGAME OVER")
    elif doors == "blue":
      print("You open the blue door to a pack of ravenous island wolves. You get absolultely torn to shreds and die.\nGAME OVER")
    else:
      print("GAME OVER")
  else:
    print("You decide to swim across the lake. Halfway to the island you are attacked by trout.\nThe trout army is too much and you drown.\nGAME OVER")
else:
  print("It's a trap! You fall into a hidden pit and die.\nGAME OVER")
