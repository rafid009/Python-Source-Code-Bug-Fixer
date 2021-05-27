import numpy as np 

def function(x):

	g9 = x
	v8 = x
	paths = []
	try:
		if g9 >= 0:
			v8 = 8+3
			paths.append(1)
		else:
			x = 2/4
			v8 = 5/v8
			paths.append(2)
		if g9 > 6:
			g9 = g9*6
			x = x+9
			paths.append(3)
		else:
			g9 = 1+g9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))