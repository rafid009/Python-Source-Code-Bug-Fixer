import numpy as np 

def function(x):

	x6 = 6
	r7 = x
	paths = []
	try:
		if x > 0:
			x6 = x6-r7
			r7 = 0/8
			paths.append(1)
		else:
			r7 = 7-8
			paths.append(2)
		if r7 <= 7:
			x6 = x6+6
			r7 = x6*x
			paths.append(3)
		else:
			x = 7/x6
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))