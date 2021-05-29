import numpy as np 

def function(x):

	a2 = 5
	r1 = x
	paths = []
	try:
		if r1 >= 8:
			a2 = r1*x
			r1 = 5+9
			x = x/1
			paths.append(1)
		else:
			a2 = a2+5
			a2 = a2+6
			paths.append(2)
		if a2 >= 0:
			a2 = 3*a2
			paths.append(3)
		else:
			a2 = 1*a2
			r1 = r1/7
			a2 = 3/r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))