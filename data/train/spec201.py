import numpy as np 

def function(x):

	a5 = x
	e2 = 2
	paths = []
	try:
		if e2 >= 0:
			e2 = e2+e2
			a5 = a5*4
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if e2 <= 5:
			x = x*e2
			paths.append(3)
		else:
			a5 = a5/a5
			a5 = 7+4
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))