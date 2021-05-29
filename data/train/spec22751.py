import numpy as np 

def function(x):

	w7 = 1
	e2 = 7
	paths = []
	try:
		if x <= 7:
			x = x*3
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if w7 >= 9:
			e2 = w7+e2
			e2 = 7*e2
			x = 2*0
			paths.append(3)
		else:
			w7 = 9/w7
			e2 = e2-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))