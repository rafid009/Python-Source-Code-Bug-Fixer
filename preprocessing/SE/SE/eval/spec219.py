import numpy as np 

def function(x):

	w1 = 8
	e0 = x
	paths = []
	try:
		if x < 0:
			w1 = w1+x
			x = x*x
			x = x*w1
			paths.append(1)
		else:
			e0 = 7+e0
			w1 = 6/w1
			e0 = e0+9
			paths.append(2)
		if x < 1:
			e0 = 4+6
			e0 = e0+8
			x = x-e0
			paths.append(3)
		else:
			w1 = e0/e0
			e0 = e0-x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		e0 = w1**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))