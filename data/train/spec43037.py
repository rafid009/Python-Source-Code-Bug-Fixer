import numpy as np 

def function(x):

	t2 = x
	g1 = 9
	paths = []
	try:
		if t2 > 4:
			t2 = t2-9
			g1 = g1+g1
			paths.append(1)
		else:
			t2 = t2-t2
			paths.append(2)
		if g1 >= 9:
			g1 = g1-1
			x = 3/x
			paths.append(3)
		else:
			g1 = g1/x
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