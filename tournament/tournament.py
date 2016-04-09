#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

class DBConn(object):

    def __init__(self):
        self.connection = psycopg2.connect("dbname=tournament")
        #http://initd.org/psycopg/docs/extras.html
        self.cursor = self.connection.cursor()

DB = DBConn()


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return DB.connection


def deleteMatches(tournament_id):
    """Remove all the match records from the database."""
    ''' NOTE: unit tests will currently break on this as i've added the tournament argument'''
    SQL = "DELETE FROM matches where tournament_id=%s"
    DB.cursor.execute(SQL, (tournament_id,))
    connection.commit()

def deletePlayers():
    """Remove all the player records from the database."""

    SQL = "DELETE FROM players"
    DB.cursor.execute(SQL)
    connection.commit()

def countPlayers():
    """Returns the number of players currently registered."""

    SQL = "SELECT count(*) FROM players"
    DB.cursor.execute(SQL)
    count = DB.cursor.fetchone()
    return count[0]

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    SQL = "INSERT INTO players (name) VALUES (%s)"
    DB.cursor.execute(SQL, (bleach.clean(name),))
    DB.connection.commit()

def playerStandings(tournamentID):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    #
    #
    #

def reportMatch(tournamentID, winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # am going to have to change the arguments of this to include
    # - tournament_id
    # - win/loss/draw stuff

def swissPairings(tournamentID):
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
