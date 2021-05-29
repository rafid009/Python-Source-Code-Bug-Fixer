import numpy as np 

def function(x):

	e6 = x
	r3 = x
	paths = []
	try:
		if r3 >= 7:
			e6 = e6*2
			paths.append(1)
		else:
			r3 = 4*1
			paths.append(2)
		if x > 1:
			r3 = e6*3
			r3 = 9+5
			paths.append(3)
		else:
			r3 = 8-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))