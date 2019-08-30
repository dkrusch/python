eye_colors = [
  {
    "color": "brown"
  },
  {
    "color": "green"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "brown"
  },
  {
    "color": "purple"
  },
  {
    "color": "purple"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  }
]

unique_eye_colors = set()

for eye in eye_colors:
    unique_eye_colors.add(eye["color"])


def get_unique_colors(eye_colors_func):
    unique_eye_colors = set()


    for eye in eye_colors_func:
        unique_eye_colors.add(eye["color"])

    return unique_eye_colors

def get_unique_colors_count(eye_colors_func):
    unique_eye_colors = set()
    eye_colors_list = []
    eye_color_count = {}


    for eye in eye_colors_func:
        eye_colors_list.append(eye["color"])
        unique_eye_colors.add(eye["color"])

    for unique_color in unique_eye_colors:
        eye_color_count.update({unique_color: eye_colors_list.count(unique_color)})

    return eye_color_count

print(get_unique_colors(eye_colors))
print(get_unique_colors_count(eye_colors))