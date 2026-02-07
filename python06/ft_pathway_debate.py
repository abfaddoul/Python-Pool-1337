# ft_pathway_debate.py

import alchemy.transmutation as transmutation

print("=== Pathway Debate Mastery ===\n")

print("Testing Absolute Imports (from basic.py):")
print("lead_to_gold():", transmutation.lead_to_gold())
print("stone_to_gem():", transmutation.stone_to_gem())

print("\nTesting Relative Imports (from advanced.py):")
print("philosophers_stone():", transmutation.philosophers_stone())
print("elixir_of_life():", transmutation.elixir_of_life())

print("\nTesting Package Access:")
print(
    "alchemy.transmutation.lead_to_gold():",
    transmutation.lead_to_gold(),
)
print(
    "alchemy.transmutation.philosophers_stone():",
    transmutation.philosophers_stone(),
)

print("\nBoth pathways work! Absolute: clear, Relative: concise")
