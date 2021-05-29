import numpy as np 

def function(x):

	q0 = x
	x2 = x
	paths = []
	try:
		if q0 >= 1:
			x = x*x2
			x = 2/x
			x2 = x2*0
			paths.append(1)
		else:
			x2 = x2+q0
			paths.append(2)
		if x < 0:
			x2 = x2/8
			x = x*7
			x = 7+x
			paths.append(3)
		else:
			x2 = 7+x2
			x = 3*x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))