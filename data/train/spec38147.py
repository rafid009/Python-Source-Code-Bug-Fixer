import numpy as np 

def function(x):

	a5 = x
	e4 = 4
	paths = []
	try:
		if e4 < 4:
			e4 = e4-a5
			a5 = a5/1
			a5 = 1/a5
			paths.append(1)
		else:
			x = 1-x
			e4 = e4*a5
			paths.append(2)
		if a5 >= 7:
			x = e4-3
			paths.append(3)
		else:
			x = x/8
			x = x+x
			x = x-2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))