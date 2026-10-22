from app.players.player import Player
from app.players.dwarves.dwarf_warrior import DwarfWarrior, Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.elf_ranger import ElfRanger, Elf
from app.players.elves.druid import Druid


def calculate_team_total_rating(players: list[Player]) -> int:
    rating_count = 0
    for player in players:
        rating_count += player.get_rating()
    return rating_count


def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
