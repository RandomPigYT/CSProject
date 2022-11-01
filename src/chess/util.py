def coordsToIndex(rank, file):
    return rank * 8 + file


def indexToCoords(index):
    return (index % 8, int(index / 8))
