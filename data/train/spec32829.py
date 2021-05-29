import numpy as np 

def function(x):

	a3 = x
	r1 = 8
	paths = []
	try:
		if a3 >= 7:
			a3 = 1+2
			x = r1/2
			paths.append(1)
		else:
			a3 = a3+1
			r1 = 5-x
			r1 = r1-0
			paths.append(2)
		if r1 < 5:
			a3 = r1-8
			paths.append(3)
		else:
			r1 = 1/r1
			a3 = a3+3
			x = 2*6
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))