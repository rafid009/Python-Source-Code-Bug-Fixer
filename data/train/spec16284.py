import numpy as np 

def function(x):

	a3 = 1
	a2 = 2
	paths = []
	try:
		if a2 < 7:
			a2 = a2*a3
			a2 = a2+a3
			a3 = a3+0
			paths.append(1)
		else:
			a3 = a3+9
			x = 8-3
			a2 = a2*a3
			paths.append(2)
		if a2 >= 5:
			a2 = a2/4
			a2 = a3-a2
			a3 = a3-5
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))