showroom = {"r32 skyline", "r32 skyline", "r34 skyline", "rx-7 fd", "mx-5"}
print(len(showroom))
showroom.update(["gtr", "370z"])
print(showroom)
showroom.discard("gtr")
print(showroom)
junkyard = {"old car 1", "old car 2", "rx-7 fd"}
junkroom = junkyard.intersection(showroom)
showyard = junkyard.union(showroom)