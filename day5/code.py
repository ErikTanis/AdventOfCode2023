def main():
    inputfile = 'input.txt'
    print('Advent of code - Day 5')
    print('Solution 1:', find_solution1(inputfile))
    print('Solution 2:', find_solution2(inputfile))

check_range = lambda n, x,y,z: n+x-y if n >= y and n < (y+z) else False

def find_solution1(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n\n')

        seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = lines
        info = [seed_soil, soil_fertilizer, fertilizer_water,
                 water_light, light_temperature, temperature_humidity, humidity_location]
        info = [i.split('\n')[1:] for i in info]
        info = [list(map(lambda x: x.split(), l)) for l in info]
        
        seeds = [int(seed) for seed in seeds.replace('seeds: ', '').split()]
        seed_dict = {seed: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None} for seed in seeds}

        for seed in seed_dict:
            for info_type in seed_dict[seed]:
                for values in info[info_type]:
                    if not values:
                        continue
                    x,y,z = map(int, values)
                    if info_type == 0:
                        previous = seed
                    else:
                        previous = seed_dict[seed][info_type -1]
                    new_num = check_range(previous,x,y,z)
                    if new_num:
                        seed_dict[seed][info_type] = new_num
                if not seed_dict[seed][info_type]:
                    if info_type == 0:
                        seed_dict[seed][info_type] = seed
                        continue
                    seed_dict[seed][info_type] = seed_dict[seed][info_type - 1]

        locations = [v[6] for v in seed_dict.values()]
        return min(locations)


def generate_seeds(seeds_start, seeds_ranges):
    for i, start in enumerate(seeds_start):
        for seed in range(start, start + seeds_ranges[i]):
            yield seed

def find_solution2(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n\n')

        seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = lines
        info = [seed_soil, soil_fertilizer, fertilizer_water,
                water_light, light_temperature, temperature_humidity, humidity_location]
        info = [i.split('\n')[1:] for i in info]
        info = [list(map(lambda x: x.split(), l)) for l in info]

        seeds = [int(seed) for seed in seeds.replace('seeds: ', '').split()]
        seeds_start = [seed for i, seed in enumerate(seeds) if i % 2 == 0]
        seeds_ranges = [seed for i, seed in enumerate(seeds) if i % 2 == 1]
        seeds = generate_seeds(seeds_start, seeds_ranges)
        lowest_loc = float('inf')

        for seed in seeds:
            seed_dict = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
            for info_type in seed_dict:
                for values in info[info_type]:
                    if not values:
                        continue
                    x, y, z = map(int, values)
                    if info_type == 0:
                        previous = seed
                    else:
                        previous = seed_dict[info_type - 1]
                    new_num = check_range(previous, x, y, z)
                    if new_num:
                        seed_dict[info_type] = new_num
                if not seed_dict[info_type]:
                    if info_type == 0:
                        seed_dict[info_type] = seed
                        continue
                    seed_dict[info_type] = seed_dict[info_type - 1]
                if info_type == 6:
                    lowest_loc = min(lowest_loc, seed_dict[info_type])
            
        return lowest_loc




if __name__ == '__main__':
    main()
