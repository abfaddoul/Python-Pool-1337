#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main():

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(x: int) -> int:
        return x

    def is_powerful(x: int) -> bool:
        return x > 10

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print("Original:", damage(10), "Amplified:", mega(10))

    print("\n=== conditional_caster ===")
    conditional_spell = conditional_caster(is_powerful, damage)
    print("Power 15:", conditional_spell(15),)
    print("Power 5:", conditional_spell(5))

    print("\n=== spell_sequence ===")
    seq = spell_sequence([fireball, heal])
    print(seq("Knight"))


if __name__ == "__main__":
    main()
