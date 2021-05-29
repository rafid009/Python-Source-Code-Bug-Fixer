import numpy as np 

def function(x):

	w4 = 7
	j7 = 6
	paths = []
	try:
		if w4 > 3:
			w4 = w4/w4
			j7 = 2*j7
			w4 = w4*2
			paths.append(1)
		else:
			x = j7+x
			w4 = 3/8
			paths.append(2)
		if w4 < 9:
			w4 = w4+5
			w4 = w4*2
			w4 = w4+9
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))