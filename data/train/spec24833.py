import numpy as np 

def function(x):

	e4 = 1
	g3 = x
	paths = []
	try:
		if g3 < 5:
			g3 = 9/g3
			e4 = 5+x
			x = x/3
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if e4 <= 7:
			x = x+6
			g3 = e4/x
			g3 = 3/g3
			paths.append(3)
		else:
			g3 = 0+e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))