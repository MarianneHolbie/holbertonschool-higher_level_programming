#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = [replace if element ==
                search else element for element in my_list]
    return (rep_list)
