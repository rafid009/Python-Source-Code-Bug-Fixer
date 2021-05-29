import numpy as np 

def function(x):

	t1 = 8
	g9 = 1
	paths = []
	try:
		if t1 > 6:
			x = x+t1
			paths.append(1)
		else:
			g9 = t1+4
			paths.append(2)
		if x <= 4:
			g9 = g9-t1
			paths.append(3)
		else:
			x = x*x
			t1 = x-3
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