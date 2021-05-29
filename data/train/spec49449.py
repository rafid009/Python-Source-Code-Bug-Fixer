import numpy as np 

def function(x):

	f4 = 7
	r7 = 9
	paths = []
	try:
		if x < 7:
			x = f4-x
			paths.append(1)
		else:
			x = 3-7
			paths.append(2)
		if f4 > 1:
			f4 = f4/x
			paths.append(3)
		else:
			x = 3/7
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