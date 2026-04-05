# Homework 3 - Board Game System
# Name: Talia Astorino
# Date: 04/05/2026
import random


def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    
    for item in data:
        print(item)


def movePlayer(data):

    currentPlayer = ""

    for item in data:
        if "Turn:" in item:
            currentPlayer = item.split(":")[1].strip()
            
    move = random.randint(1, 6)
    print("\n" + currentPlayer + " rolled a", move)
    
    newData = []

    for item in data:
        if currentPlayer in item and "Turn" not in item:
            parts = item.split(":")
            position = int(parts[0].strip())
            player = parts[1].strip()

            newPosition = position + move

            if newPosition > 25:
                newPosition = 25

            print(player, "moved to space", newPosition)

            for eventItem in data:
                if "Candy" in eventItem or "Mud" in eventItem or "Rainbow" in eventItem or "Swamp" in eventItem:
                    eventParts = eventItem.split(":")
                    eventPosition = int(eventParts[0].strip())
                    eventName = eventParts[1].strip()

                    if newPosition == eventPosition:
                        print(player, "landed on", eventName)

                        if eventName == "Candy":
                            newPosition += 2
                            print(player, "moves forward 2 spaces!")
                        elif eventName == "Mud":
                            newPosition -= 2
                            print(player, "moves backward 2 spaces!")
                        elif eventName == "Rainbow":
                            newPosition += 3
                            print(player, "moves forward 3 spaces!")
                        elif eventName == "Swamp":
                            print(player, "loses next turn!")
                            
            if newPosition < 1:
                newPosition = 1

            if newPosition > 25:
                newPosition = 25

            newItem = str(newPosition) + ": " + player
            newData.append(newItem)

        elif "Turn:" in item:
            if currentPlayer == "Player1":
                newData.append("Turn: Player2")
            else:
                newData.append("Turn: Player1")

        else:
            newData.append(item)

    return newData
def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)

    playing = True

    while playing:
        displayGame(gameData)

        choice = input("\nMove player? (y/n): ")
        
        if choice.lower() == "y":
            gameData = movePlayer(gameData)

            winner = ""

            for item in gameData:
                if "Player1" in item and "Turn" not in item:
                    position = int(item.split(":")[0].strip())
                    if position >= 25:
                        winner = "Player1"

                elif "Player2" in item and "Turn" not in item:
                    position = int(item.split(":")[0].strip())
                    if position >= 25:
                        winner = "Player2"

            print("\nUpdated Game State:")
            displayGame(gameData)

            if winner != "":
                print("\n" + winner + " wins the game!")
                playing = False

        else:
            playing = False


if __name__ == "__main__":
    main()
