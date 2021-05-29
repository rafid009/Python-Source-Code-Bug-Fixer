import numpy as np 

def function(x):

	g8 = x
	v4 = x
	paths = []
	try:
		if x < 8:
			v4 = 9/4
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if v4 > 9:
			x = v4*x
			v4 = 8-v4
			paths.append(3)
		else:
			g8 = x+g8
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))