import random
from choises.story import user_stories, story_locations, story_items, story_events

#Apartado para el comando story
async def tell_story(user_id: int):

    location = random.choice(story_locations)
    item = random.choice(story_items)
    event = random.choice(story_events)

    user_stories[user_id] = {
        "location": location,
        "item": item,
        "event": event
    }
    return  (f"You wake up in {location}.\n\n"
            f"Next to you is {item}.\n\n"
            f"{event}\n\n"
            "What do you do?")