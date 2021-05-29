import numpy as np 

def function(x):

	e0 = x
	w2 = x
	paths = []
	try:
		if e0 > 5:
			x = x-e0
			x = x+4
			paths.append(1)
		else:
			w2 = 2*w2
			e0 = 3*e0
			w2 = 2/w2
			paths.append(2)
		if e0 < 5:
			x = x+1
			paths.append(3)
		else:
			w2 = e0/w2
			x = 9-e0
			e0 = e0+0
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		e0 = w2**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))