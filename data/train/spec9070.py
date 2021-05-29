import numpy as np 

def function(x):

	q9 = 7
	r1 = 5
	x = 9
	paths = []
	try:
		if r1 > 6:
			x = 2/1
			r1 = 1+r1
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if q9 >= 0:
			x = 2-5
			r1 = 3+x
			paths.append(3)
		else:
			x = x-0
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