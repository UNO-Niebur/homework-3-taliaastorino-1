# Homework 3 - Board Game System
# Name:
# Date:

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
    """Moves Player1 forward by a chosen amount."""
    move = int(input("\nHow many spaces should Player1 move? "))

    newData = []

    for item in data:
        if "Player1" in item:
            parts = item.split(":")
            position = int(parts[0].strip())
            player = parts[1].strip()

            newPosition = position + move

            if newPosition > 25:
                newPosition = 25

            print(player, "moved to space", newPosition)

            eventFound = False

            for eventItem in data:
                if "Candy" in eventItem or "Mud" in eventItem or "Rainbow" in eventItem or "Swamp" in eventItem:
                    eventParts = eventItem.split(":")
                    eventPosition = int(eventParts[0].strip())
                    eventName = eventParts[1].strip()

                    if newPosition == eventPosition:
                        eventFound = True
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

        else:
            newData.append(item)

    return newData
def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        gameData = movePlayer(gameData)

        print("\nUpdated Game State:")
        displayGame(gameData)


if __name__ == "__main__":
    main()
