import numpy as np 

def function(x):

	w1 = x
	a2 = x
	paths = []
	try:
		if a2 > 4:
			w1 = x/3
			x = 3-x
			a2 = a2/2
			paths.append(1)
		else:
			w1 = w1*1
			a2 = 0-w1
			paths.append(2)
		if a2 <= 1:
			w1 = w1/a2
			w1 = 7*8
			paths.append(3)
		else:
			x = 6/w1
			x = 3*x
			x = 6+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))