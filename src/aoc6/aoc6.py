from src.aoc6.boat_race import BoatRace

if __name__ == '__main__':
    # Puzzle Input
    # Time:        35     93     73     66
    # Distance:   212   2060   1201   1044
    max_durations = [35, 93, 73, 66]
    distance_records = [212, 2060, 1201, 1044]

    part1 = BoatRace.error_margins_for_race(max_durations, distance_records)

    print(f"The product of all number of ways to beat each race = {part1}\n\n")

    # time: 35937366
    # distance: 212206012011044
    part2 = BoatRace.ways_by_min_max(35937366, 212206012011044)

    print(f"The race can be beat in {part2} number of ways!\n")
