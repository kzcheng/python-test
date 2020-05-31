import pprint
pp = pprint.PrettyPrinter().pprint


def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_10 = create_adder(10)
# => 13

pp(add_10(3))

pp("FUCK")


coordinates = [
    {
        "name": "Location 1",
        "gps": (29.008966, 111.573724)
    },
    {
        "name": "Location 2",
        "gps": (40.1632626, 44.2935926)
    },
    {
        "name": "Location 3",
        "gps": (29.476705, 121.869339)
    }
]

pp(coordinates)
