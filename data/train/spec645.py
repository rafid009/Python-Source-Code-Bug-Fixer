import numpy as np 

def function(x):

	t2 = 3
	g0 = x
	paths = []
	try:
		if g0 > 5:
			x = x-8
			t2 = 2-4
			paths.append(1)
		else:
			t2 = t2-g0
			paths.append(2)
		if x < 3:
			t2 = 0-t2
			g0 = g0+g0
			x = t2-x
			paths.append(3)
		else:
			x = 1/9
			x = x-3
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))