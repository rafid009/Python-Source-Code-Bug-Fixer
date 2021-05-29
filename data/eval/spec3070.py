import numpy as np 

def function(x):

	e0 = 2
	r7 = 9
	x = x
	paths = []
	try:
		if x < 8:
			x = x*0
			x = e0-x
			paths.append(1)
		else:
			r7 = 0/r7
			e0 = 7+2
			paths.append(2)
		if x <= 5:
			x = x-3
			r7 = 7-6
			paths.append(3)
		else:
			x = r7/1
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