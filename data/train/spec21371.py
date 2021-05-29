import numpy as np 

def function(x):

	a7 = 9
	e6 = x
	paths = []
	try:
		if x <= 1:
			x = 7+x
			x = 3/x
			paths.append(1)
		else:
			x = e6-e6
			paths.append(2)
		if e6 >= 4:
			a7 = a7+e6
			e6 = x*e6
			paths.append(3)
		else:
			x = x/8
			a7 = a7-3
			x = x-8
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		a7 = e6**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))