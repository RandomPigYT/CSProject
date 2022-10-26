from chess import globals as g
from chess import util


def distToEdge():
    rank = 0

    while rank < 8:
        file = 0

        while file < 8:
            index = util.coordsToIndex(rank, file)

            distNorth = 7 - rank
            distSouth = rank
            distEast = 7 - file
            distWest = file

            distNorthEast = min(distNorth, distEast)
            distNorthWest = min(distNorth, distWest)
            distSouthEast = min(distSouth, distEast)
            distSouthWest = min(distSouth, distWest)

            g.distToEdge.append(
                (
                    distNorth,
                    distSouth,
                    distEast,
                    distWest,
                    distNorthEast,
                    distNorthWest,
                    distSouthEast,
                    distSouthWest,
                )
            )

            file += 1

        rank += 1
