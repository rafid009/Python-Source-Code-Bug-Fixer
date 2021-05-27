import numpy as np 

def function(x):

	w1 = 9
	e0 = x
	paths = []
	try:
		if x <= 9:
			e0 = e0*1
			x = 6+w1
			paths.append(1)
		else:
			w1 = w1+e0
			w1 = w1+9
			paths.append(2)
		if w1 <= 8:
			e0 = 5*e0
			paths.append(3)
		else:
			x = 3-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))