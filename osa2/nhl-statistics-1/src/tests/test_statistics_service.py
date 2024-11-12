import unittest
from statistics_service import StatisticsService
from player import Player

# Stub-luokka, joka ei käytä verkkoyhteyttä
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

# Testiluokka StatisticsService-luokalle
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Injektoi stub-olio StatisticsService-oliolle
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")
    
    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_players_of_team(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertEqual(team_players[0].team, "EDM")

    def test_team_returns_empty_list_if_team_not_found(self):
        team_players = self.stats.team("NYR")
        self.assertEqual(len(team_players), 0)

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 2)

    def test_top_returns_players_sorted_by_points(self):
        top_players = self.stats.top(3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")