from choises.support_responses import support_responses

async def support_responses(message: str):

    text = message.lower()

    for keyword, responses in support_responses.items():
        if keyword in text:
            response = random.choice(responses)

            return(
                f"{response}\n\n"
                "I'm a bot, not a therapist or medical professional. "
                "If you need personal support, consider talking with "
                "someone you trust."
            )

    return(
        "It sounds like something is bothering you. "
        "I can offer general wellness suggestions, but I'm not a therapist. "
        "If you need personal support, consider reaching out to someone you trust."
    )