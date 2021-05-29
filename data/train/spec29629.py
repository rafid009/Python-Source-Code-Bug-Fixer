import numpy as np 

def function(x):

	e0 = x
	l3 = 1
	paths = []
	try:
		if e0 < 2:
			x = 5+x
			paths.append(1)
		else:
			x = 2-l3
			l3 = 9-l3
			paths.append(2)
		if x >= 7:
			l3 = 8-9
			paths.append(3)
		else:
			e0 = e0-7
			x = e0/8
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))