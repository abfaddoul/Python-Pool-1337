#!/usr/bin/env python3
"""Inventory Master - Manage inventories using dictionaries only (ex4)."""


def compute_inventory_value(inventory):
    """Compute total inventory value (sum of qty * value)."""
    total = 0
    for _, data in inventory.items():
        total += data["qty"] * data["value"]
    return total


def compute_item_count(inventory):
    """Compute total item count (sum of qty)."""
    total = 0
    for _, data in inventory.items():
        total += data["qty"]
    return total


def build_category_summary(inventory):
    """Return a dict mapping category -> total qty in that category."""
    categories = {}
    for _, data in inventory.items():
        category = data["category"]
        qty = data["qty"]
        categories[category] = categories.get(category, 0) + qty
    return categories


def print_inventory(player_name, inventory):
    """Print a formatted inventory report for a player."""
    print(f"=== {player_name}'s Inventory ===")

    for item_name, data in inventory.items():
        category = data["category"]
        rarity = data["rarity"]
        qty = data["qty"]
        value = data["value"]
        item_total = qty * value

        print(
            f"{item_name} ({category}, {rarity}): "
            f"{qty}x @ {value} gold each = {item_total} gold"
        )

    total_value = compute_inventory_value(inventory)
    total_items = compute_item_count(inventory)
    categories = build_category_summary(inventory)

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    parts = []
    for cat, count in categories.items():
        parts.append(f"{cat}({count})")
    print(f"Categories: {', '.join(parts)}")


def transfer_item(from_inv, to_inv, item_name, qty):
    """Transfer qty of item_name from from_inv to to_inv.

    Returns True if successful, False otherwise.
    """
    if qty <= 0:
        return False

    from_item = from_inv.get(item_name)
    if from_item is None:
        return False

    if from_item["qty"] < qty:
        return False

    # Remove from sender
    from_item["qty"] -= qty

    # Add to receiver (create if missing)
    to_item = to_inv.get(item_name)
    if to_item is None:
        to_inv[item_name] = {
            "category": from_item["category"],
            "rarity": from_item["rarity"],
            "qty": qty,
            "value": from_item["value"],
        }
    else:
        to_item["qty"] += qty

    return True


def most_valuable_player(players):
    """Return (name, total_value) of most valuable inventory."""
    best_name = ""
    best_value = -1

    for name, inv in players.items():
        value = compute_inventory_value(inv)
        if value > best_value:
            best_value = value
            best_name = name

    return best_name, best_value


def most_items_player(players):
    """Return (name, total_items) of player with most total qty."""
    best_name = ""
    best_count = -1

    for name, inv in players.items():
        count = compute_item_count(inv)
        if count > best_count:
            best_count = count
            best_name = name

    return best_name, best_count


def rarest_items(players):
    """Return a comma-separated string of rare items
    owned by exactly one player.
    """
    ownership = {}

    for _, inv in players.items():
        for item_name, data in inv.items():
            if data["rarity"] != "rare":
                continue
            ownership[item_name] = ownership.get(item_name, 0) + 1

    parts = []
    for item_name, count in ownership.items():
        if count == 1:
            parts.append(item_name)

    return ", ".join(parts)


def main():
    """Run the inventory demo matching the subject's scenario."""
    print("=== Player Inventory System ===")

    alice_inventory = {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "qty": 1,
            "value": 500,
        },

        "potion": {
            "category": "consumable",
            "rarity": "common",
            "qty": 5,
            "value": 50,
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "qty": 1,
            "value": 200,
        },
    }

    bob_inventory = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "qty": 1,
            "value": 300,
        }
    }

    players = {}
    players.update({"Alice": alice_inventory})
    players.update({"Bob": bob_inventory})

    print_inventory("Alice", alice_inventory)

    print("=== Transaction: Alice gives Bob 2 potions ===")
    if transfer_item(alice_inventory, bob_inventory, "potion", 2):
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    alice_potions = alice_inventory.get("potion", {}).get("qty", 0)
    bob_potions = bob_inventory.get("potion", {}).get("qty", 0)
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")

    print("=== Inventory Analytics ===")
    name, value = most_valuable_player(players)
    print(f"Most valuable player: {name} ({value} gold)")

    name, count = most_items_player(players)
    print(f"Most items: {name} ({count} items)")

    print(f"Rarest items: {rarest_items(players)}")


if __name__ == "__main__":
    main()
