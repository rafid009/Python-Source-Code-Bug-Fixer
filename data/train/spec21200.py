import numpy as np 

def function(x):

	e0 = x
	w6 = x
	paths = []
	try:
		if w6 >= 1:
			x = x*x
			e0 = e0-e0
			e0 = 4-e0
			paths.append(1)
		else:
			w6 = w6-2
			w6 = w6-9
			paths.append(2)
		if x >= 8:
			w6 = 9-8
			e0 = 4*2
			paths.append(3)
		else:
			e0 = e0-5
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		w6 = e0**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))