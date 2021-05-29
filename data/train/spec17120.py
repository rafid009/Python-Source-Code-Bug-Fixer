import numpy as np 

def function(x):

	a3 = 1
	e6 = 0
	paths = []
	try:
		if x < 7:
			a3 = 4/x
			paths.append(1)
		else:
			a3 = a3*a3
			x = x*3
			paths.append(2)
		if e6 > 7:
			a3 = 6*a3
			x = 2-e6
			paths.append(3)
		else:
			e6 = e6*a3
			x = x*3
			e6 = e6-a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))