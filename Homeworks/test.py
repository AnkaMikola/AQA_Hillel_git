# adventures_of_tom_sawer = """\
# Tom gave up the brush with reluctance in his .... face but alacrity
# in his heart. And while
# the late steamer
# "Big Missouri" worked ....
# and sweated
# in the sun,
# the retired artist sat on a barrel in the .... shade close by, dangled his legs,
# munched his apple, and planned the slaughter of more innocents.
# There was no lack of material;
# boys happened along every little while;
# they came to jeer, but .... remained to whitewash. ....
# By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
# a kite, in good repair;
# and when he played
# out, Johnny Miller bought
# in for a dead rat and a string to swing it with—and so on, and so on,
# hour after hour. And when the middle of the afternoon came, from being a
# poor poverty, stricken boy in the .... morning, Tom was literally
# rolling in wealth."""
#
# ##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# # task 01 ==
# """ Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# # adventures_of_tom_sawer.replace("\n", " ")
# # print(adventures_of_tom_sawer)
#
# # task 02 ==
# """ Замініть .... на пробіл
# """
# adventures_of_tom_sawer_1 = adventures_of_tom_sawer.replace(' .... ', ' ')
# print(adventures_of_tom_sawer_1)

TASK_START_TEMPLATE = '---Task {0} ----\n'
print(TASK_START_TEMPLATE.format(1))
print(TASK_START_TEMPLATE.format(2))