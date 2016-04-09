P2 Tournament
=============

Provides a database and functions to hold a swiss-system tournament.

Two tables exist: a players database (storing player names and IDs) and a 
matches database (storing match IDs and player outcomes for all tournaments).

Functions
=========

Player management functions:

- registerPLayers(name) will create a new player entry with ID for the given player. Duplicates
    are allowed, as players will receive unique IDs.

- deletePlayers() remove all players from the database.

- countPlayers() returns the number of players currently registered in the database.


Match functions:

- deleteMatches(tournament_id) deletes all matches for the given tournament.

Tournament functions (TODO:)

- reportMatch(tournamentID, args???) to record the outcome of a single match.

- playerStandings(tournament_id) returns a list of the players sorted by their 
win records for the given tournament_id.

- swissPairings(tournament_id) returns a list of pairings for the next round.

