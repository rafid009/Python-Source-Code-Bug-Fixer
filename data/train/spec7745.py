import numpy as np 

def function(x):

	g9 = 9
	j4 = x
	paths = []
	try:
		if j4 < 6:
			g9 = x/j4
			paths.append(1)
		else:
			g9 = g9+9
			g9 = g9/3
			g9 = g9/5
			paths.append(2)
		if j4 > 5:
			g9 = j4+0
			j4 = j4/9
			paths.append(3)
		else:
			x = 5*x
			j4 = 4-x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))