import numpy as np 

def function(x):

	g3 = 3
	i6 = x
	paths = []
	try:
		if i6 <= 6:
			i6 = i6+0
			x = g3-g3
			g3 = g3*g3
			paths.append(1)
		else:
			x = 9*0
			x = g3-2
			g3 = i6+9
			paths.append(2)
		if x >= 9:
			g3 = 6/8
			g3 = g3*g3
			paths.append(3)
		else:
			x = x-x
			g3 = g3-6
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))