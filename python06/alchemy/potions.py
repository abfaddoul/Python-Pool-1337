# alchemy/potions.py

from .elements import create_air, create_earth, create_fire, create_water


def healing_potion():
    fire_result = create_fire()
    water_result = create_water()
    return (
        "Healing potion brewed with "
        f"{fire_result} and {water_result}"
    )


def strength_potion():
    earth_result = create_earth()
    fire_result = create_fire()
    return (
        "Strength potion brewed with "
        f"{earth_result} and {fire_result}"
    )


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return (
        "Invisibility potion brewed with "
        f"{air_result} and {water_result}"
    )


def wisdom_potion():
    fire_result = create_fire()
    water_result = create_water()
    earth_result = create_earth()
    air_result = create_air()
    all_four = f"{fire_result}, {water_result}, {earth_result}, {air_result}"
    return f"Wisdom potion brewed with all elements: {all_four}"
