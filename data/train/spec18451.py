import numpy as np 

def function(x):

	w6 = x
	e0 = 9
	paths = []
	try:
		if e0 > 6:
			e0 = 9/e0
			paths.append(1)
		else:
			x = x-6
			x = x-0
			paths.append(2)
		if e0 < 1:
			e0 = e0+w6
			w6 = w6/2
			paths.append(3)
		else:
			w6 = w6+e0
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))