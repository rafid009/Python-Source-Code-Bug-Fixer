import numpy as np 

def function(x):

	e1 = 3
	a0 = x
	paths = []
	try:
		if a0 >= 8:
			e1 = e1*6
			e1 = e1/8
			paths.append(1)
		else:
			a0 = 5/a0
			a0 = a0/8
			paths.append(2)
		if e1 <= 5:
			a0 = 9*a0
			paths.append(3)
		else:
			a0 = 6-a0
			a0 = x+a0
			a0 = 6*a0
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