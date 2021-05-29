import numpy as np 

def function(x):

	i3 = x
	g6 = 4
	x = x
	paths = []
	try:
		if g6 <= 2:
			i3 = i3/4
			x = x*i3
			x = x-3
			paths.append(1)
		else:
			x = x*g6
			x = 4-5
			paths.append(2)
		if i3 <= 2:
			g6 = g6-0
			g6 = 3-2
			paths.append(3)
		else:
			x = i3/i3
			i3 = 4-x
			g6 = g6+8
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		g6 = i3**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))