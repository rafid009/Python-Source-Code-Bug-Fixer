import numpy as np 

def function(x):

	d7 = 9
	a1 = x
	paths = []
	try:
		if a1 > 6:
			a1 = 4+5
			d7 = 7+8
			paths.append(1)
		else:
			a1 = d7/a1
			paths.append(2)
		if x <= 4:
			a1 = a1*8
			paths.append(3)
		else:
			a1 = x/d7
			a1 = 0-2
			d7 = 5-0
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