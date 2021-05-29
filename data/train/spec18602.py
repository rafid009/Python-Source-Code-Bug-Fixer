import numpy as np 

def function(x):

	e6 = 3
	a4 = 4
	paths = []
	try:
		if e6 > 2:
			a4 = 5/a4
			e6 = e6+3
			x = x+a4
			paths.append(1)
		else:
			a4 = a4+x
			paths.append(2)
		if x < 1:
			a4 = a4-4
			paths.append(3)
		else:
			a4 = 5+4
			x = x/3
			e6 = 8+e6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))