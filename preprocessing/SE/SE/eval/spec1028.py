import numpy as np 

def function(x):

	r2 = 6
	g3 = x
	paths = []
	try:
		if x <= 2:
			r2 = x+5
			paths.append(1)
		else:
			g3 = x*7
			paths.append(2)
		if x < 7:
			x = x-r2
			paths.append(3)
		else:
			g3 = 0/g3
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		g3 = r2**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))