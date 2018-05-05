#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyemtapi


idClient = 'You idClient'
passKey = 'You passKey'

api = pyemtapi.EMT(idClient, passKey)

# Returns a line/s route with the vertex info to build the route and coordinates for stops and axes
print(api.GetRouteLines("04/05/2018", "26|27"))

# Get line route with vertex info to build map and coordinates for Stops
print(api.GetRouteLinesRoute("04/05/2018", "26|27"))

# Get EMT Calendar for all days and line schedules for a range of dates
print(api.GetCalendar("04/05/2018","05/05/2018"))

# Returns lines with description and group
print(api.GetListLines("05/05/2018", "26|27"))

# Returns lines with description and group
print(api.GetListLinesExtend("05/05/2018", "26|27"))

# Return a list of groups
print(api.GetGroups())

# Returns current schedules for the requested lines
print(api.GetTimesLines("04/05/2018", "26|27"))

# Provide information of the requested line with a trip-level detail.
print(api.GetTimeTableLines("04/05/2018", "26|27"))

# Returns all stop identifiers and his coordinate, name, lines and directions
print(api.GetNodesLines(1))

# Returns a list of EMT nodes related to a location. All EMT locations are a group of stops within a target radius and
# the lines related to each stop in the list
print(api.GetStreet("Mayor", 10))

# Returns a list of stops from a target stop with a target radius and the lines arriving to those stops.
print(api.GetStopsFromStop(23,2))

# Returns a list of stops from a coordinate with a radius and the lines arriving to those stops
print(api.GetStopsFromXY("40.429416", "-3.6895", 100))

# Gets bus arrive info to a target stop
print(api.GetArriveStop(1))

# Returns a list of Point of interest types
print(api.GetPointsOfInterestTypes())

# Returns a list of Points of Interest from a coordinate center with a target radius
print(api.GetPointsOfInterest("40.429416","-3.6895", 100))

# Returns a list of stops from a target coordinate
print(api.getStreetFromXY("40.429416", "-3.6895", 100))

# Returns line info in a target date
print(api.GetInfoLine("04/05/2018", 26))

# Returns line info in a target date
print(api.GetInfoLineExtend("04/05/2018", 26))

# Returns a list of stops related to a line with an optional direction
print(api.GetStopsLine(26,1))

# Returns the relationship of exploitation groups
print(api.GeoGetGroups())




