import numpy as np 

def function(x):

	b3 = x
	w1 = 4
	paths = []
	try:
		if w1 < 2:
			w1 = b3/w1
			paths.append(1)
		else:
			b3 = b3-6
			paths.append(2)
		if b3 < 8:
			w1 = 1+b3
			w1 = x*x
			paths.append(3)
		else:
			b3 = 9*b3
			w1 = 3+w1
			w1 = 4+b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		w1 = b3**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))