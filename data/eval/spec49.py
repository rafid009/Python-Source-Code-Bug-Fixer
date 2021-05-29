import numpy as np 

def function(x):

	f9 = x
	r3 = 3
	paths = []
	try:
		if r3 >= 2:
			r3 = r3/r3
			paths.append(1)
		else:
			r3 = r3-r3
			x = 6*1
			paths.append(2)
		if x <= 7:
			f9 = 1+6
			f9 = f9-x
			paths.append(3)
		else:
			r3 = 3+r3
			x = 4+5
			r3 = r3-f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))