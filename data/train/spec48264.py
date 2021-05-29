import numpy as np 

def function(x):

	e0 = 1
	o2 = x
	paths = []
	try:
		if e0 <= 0:
			x = x+0
			e0 = 0/e0
			paths.append(1)
		else:
			e0 = 2+e0
			e0 = 8-6
			paths.append(2)
		if e0 < 0:
			x = x/o2
			paths.append(3)
		else:
			e0 = e0+o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		e0 = o2**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))