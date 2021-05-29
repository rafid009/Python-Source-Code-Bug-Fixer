import numpy as np 

def function(x):

	i3 = 2
	g0 = x
	paths = []
	try:
		if g0 >= 1:
			g0 = 6/g0
			paths.append(1)
		else:
			i3 = 9-i3
			paths.append(2)
		if i3 <= 0:
			x = x/4
			i3 = i3-g0
			paths.append(3)
		else:
			g0 = i3-g0
			x = x+5
			g0 = g0+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))