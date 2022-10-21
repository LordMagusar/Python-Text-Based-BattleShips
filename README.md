# Python-Text-Based-BattleShips

It's battleships, in the Python console

Game starts with the player inputting all positions of their ships

Full disclosure, this is incredibly easy to break. There is *some* error handling that catches cooridinates being put in places that don't make sense (Eg coord 1 = A2, coord 2 = G7), however L shaped ships are very possible

Ships are all stored in the players repective dictionary. Eg, P1ships is a dictionary, containg the Key "Carrier". The value for this key is an array of arrays containing all of the carries coordinates, and their hit/sunk status

CPU's AI hits random spots until it hits a ship. When it does, it attempts to hit adjacent squares in order to sink the ship

It does this by adding all possible adjacent coordinates to an array. This is done by a fairly lengthy try except chain, in order to access whether or not the coordinates are valid.



OS.SYSTEM IS ONLY USED TO CLEAR THE CONSOLE
