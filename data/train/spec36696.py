import numpy as np 

def function(x):

	d4 = x
	r5 = x
	paths = []
	try:
		if d4 < 3:
			x = 9-x
			x = x-2
			paths.append(1)
		else:
			d4 = 7-4
			paths.append(2)
		if x >= 8:
			x = x+4
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))