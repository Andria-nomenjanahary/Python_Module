#!/usr/bin/python3
import alchemy.grimoire.dark_spellbook

if __name__ == "__main__":
    check = alchemy.grimoire.dark_spellbook.\
        dark_spell_record("Fantasy", "Earth, wind and fire")
    print("Testing record light spell:", end="")
    print(f" {check}")
