import numpy as np 

def function(x):

	w1 = 2
	a2 = x
	paths = []
	try:
		if a2 > 4:
			w1 = a2-w1
			a2 = a2/a2
			paths.append(1)
		else:
			x = a2-w1
			w1 = w1+8
			paths.append(2)
		if a2 >= 9:
			x = x+x
			paths.append(3)
		else:
			w1 = 9*x
			x = w1+x
			w1 = a2*w1
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))