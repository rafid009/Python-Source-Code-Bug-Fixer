import numpy as np 

def function(x):

	g6 = x
	r2 = 7
	x = x
	paths = []
	try:
		if r2 <= 4:
			x = g6-r2
			g6 = g6/6
			g6 = 9+9
			paths.append(1)
		else:
			x = g6+9
			r2 = r2*4
			paths.append(2)
		if x <= 8:
			x = x*x
			r2 = 0+r2
			g6 = g6/7
			paths.append(3)
		else:
			g6 = g6+x
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))