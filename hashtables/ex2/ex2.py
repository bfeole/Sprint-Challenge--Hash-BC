#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert source and destination from tickets into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # set first value of route to value of source/key none(LAX)
    route[0] = hash_table_retrieve(hashtable, "NONE")
    # starting at index 1 of route,
    # retrieve saved key source value of previous index position,
    # set equal to current route index
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    return route
