from app.battle import Battle
from app.charcters.knightinfo import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight.from_dict(config)
        for name, config in knights_config.items()
    }
    for knight in knights.values():
        knight.prepare_for_battle()

    Battle.fight(knights["Lancelot"], knights["Mordred"])
    Battle.fight(knights["Arthur"], knights["Red Knight"])

    return {name: knight.hp for name, knight in knights.items()}
