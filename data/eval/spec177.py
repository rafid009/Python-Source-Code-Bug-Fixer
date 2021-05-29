import numpy as np 

def function(x):

	e6 = x
	a2 = x
	paths = []
	try:
		if x > 7:
			a2 = a2/x
			a2 = e6+x
			x = 9-1
			paths.append(1)
		else:
			e6 = e6-0
			a2 = a2+6
			paths.append(2)
		if a2 >= 8:
			e6 = 9*6
			a2 = e6+x
			a2 = e6-x
			paths.append(3)
		else:
			e6 = e6+a2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		a2 = e6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))