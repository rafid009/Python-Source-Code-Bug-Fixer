import numpy as np 

def function(x):

	w1 = x
	e5 = x
	paths = []
	try:
		if x <= 8:
			w1 = x-w1
			e5 = 5+e5
			paths.append(1)
		else:
			w1 = w1*4
			paths.append(2)
		if e5 <= 9:
			x = 4+x
			x = x+2
			paths.append(3)
		else:
			x = x*9
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