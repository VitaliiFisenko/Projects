import random
import curses

s = curses.initsrc()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh,sw,0,0)

