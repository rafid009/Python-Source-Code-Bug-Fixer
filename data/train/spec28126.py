import numpy as np 

def function(x):

	e6 = 0
	a0 = x
	paths = []
	try:
		if e6 < 8:
			a0 = a0*4
			paths.append(1)
		else:
			x = 6+a0
			a0 = a0+e6
			x = 5+x
			paths.append(2)
		if x > 3:
			a0 = 4-1
			paths.append(3)
		else:
			e6 = 7+e6
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))