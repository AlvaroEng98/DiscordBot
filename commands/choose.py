async def select_choose(user_id : int, choice : str):

    choice = choice.lower()

    if choice == "left":
        response = (
            "You head left and discover a room filled with old maps. "
            "One of them has your name written on it."
        )

    elif choice == "right":
        response = (
            "You head right and find a staircase leading toward "
            "a strange blue light."
        )

    else:
        response = "Try choosing `left` or `right`."

    return response