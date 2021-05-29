import numpy as np 

def function(x):

	p2 = 3
	t8 = 9
	paths = []
	try:
		if t8 > 6:
			t8 = 1/t8
			t8 = t8/p2
			paths.append(1)
		else:
			x = x+6
			p2 = x-7
			paths.append(2)
		if p2 > 8:
			t8 = 7+t8
			paths.append(3)
		else:
			p2 = 6*4
			x = t8-x
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