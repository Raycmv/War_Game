from area_surface import *

ACTIONS = [
	
	["sea_map", lambda: Area_surface('mundo//sea_map.png', 0, 0, 0, 0, 5000, 10000, WORLD_WIDTH, WORLD_HEIGHT, "sea")],
    ["land_map", lambda: Area_surface('mundo//land_map.png', LAND_X, LAND_Y, 400, 605, 4335, 9095, LAND_WIDTH, LAND_HEIGHT, "land")],
    ["Erantia", lambda: Area_surface('mundo//land_map_area.png', 5485, 10685, 4010, 7080, 2050, 2210, 4095, 4415, "Erantia")],
    ["Andortia", lambda: Area_surface('mundo//land_map_area.png', 545, 775, 70, 80, 2190, 1970, 4380, 3930, "Andortia")],
    ["Fenitha", lambda: Area_surface('mundo//land_map_area.png', 3690, 1060, 2860, 100, 3100, 2770, 6198, 5533, "Fenitha")],
    ["Kryvenia", lambda: Area_surface('mundo//land_map_area.png', 525, 3600, 70, 2210, 2160, 1960, 4310, 3920, "Kryvenia")],
    ["Lumaris", lambda: Area_surface('mundo//land_map_area.png', 5240, 3990, 3485, 2955, 1835, 2015, 3670, 4030, "Lumaris")],
    ["Novrita", lambda: Area_surface('mundo//land_map_area.png', 390, 7560, 205, 4420, 1815, 1980, 3630, 3960, "Novrita")],
    ["Ostravel", lambda: Area_surface('mundo//land_map_area.png', 2975, 7135, 2140, 5040, 1590, 2685, 3180, 5370, "Ostravel")],
    ["Toranilis", lambda: Area_surface('mundo//land_map_area.png', 5635, 7885, 3890, 5250, 1910, 1840, 3815, 3670, "Toranilis")],
    ["Valmorino", lambda: Area_surface('mundo//land_map_area.png', 435, 11265, 90, 7320, 2325, 2440, 4645, 4880, "Valmorino")],
    ["Suricem", lambda: Area_surface('mundo//land_map_area.png', 620, 14985, 1595, 9535, 3725, 2345, 7445, 4690, "Suricem")]
]