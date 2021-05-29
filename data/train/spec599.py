import numpy as np 

def function(x):

	w2 = x
	e2 = 1
	paths = []
	try:
		if x <= 3:
			w2 = e2+w2
			w2 = 8+w2
			paths.append(1)
		else:
			x = 6*x
			w2 = x-8
			e2 = 9/x
			paths.append(2)
		if x < 2:
			e2 = e2-5
			w2 = w2-2
			e2 = e2-4
			paths.append(3)
		else:
			w2 = w2+2
			x = w2-1
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		e2 = w2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))