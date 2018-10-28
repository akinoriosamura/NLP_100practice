# coding: utf-8

import re

target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
target_list = target.split(" ")
target_list_alpha = list(map(lambda t: re.sub("[^a-zA-Z]", '', t), target_list))

print(target_list_alpha)

l_target_list = list(map(lambda t: len(t), target_list_alpha))
print(l_target_list)
