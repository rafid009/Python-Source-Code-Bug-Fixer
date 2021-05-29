import numpy as np 

def function(x):

	w6 = x
	e0 = x
	paths = []
	try:
		if e0 <= 8:
			w6 = w6*x
			paths.append(1)
		else:
			e0 = e0-6
			w6 = w6*w6
			w6 = x*w6
			paths.append(2)
		if e0 <= 7:
			x = x+1
			w6 = w6+8
			paths.append(3)
		else:
			e0 = e0-6
			x = 1*2
			x = e0/6
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