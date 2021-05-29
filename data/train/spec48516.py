import numpy as np 

def function(x):

	a2 = x
	w2 = x
	paths = []
	try:
		if a2 >= 7:
			w2 = 6+x
			a2 = w2+3
			paths.append(1)
		else:
			w2 = 6+0
			paths.append(2)
		if w2 >= 2:
			w2 = w2*w2
			w2 = 1*w2
			w2 = 3/x
			paths.append(3)
		else:
			x = a2-x
			x = x-2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))