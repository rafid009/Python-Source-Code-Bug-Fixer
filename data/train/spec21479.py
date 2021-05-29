import numpy as np 

def function(x):

	g9 = 1
	o3 = 1
	paths = []
	try:
		if x >= 0:
			g9 = 5+9
			x = 1*0
			paths.append(1)
		else:
			g9 = g9*4
			x = x+9
			x = x/g9
			paths.append(2)
		if x > 5:
			g9 = g9+g9
			o3 = 0*4
			paths.append(3)
		else:
			g9 = 5*g9
			x = x/4
			o3 = o3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))