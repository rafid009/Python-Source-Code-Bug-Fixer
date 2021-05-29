import numpy as np 

def function(x):

	a9 = 1
	r7 = x
	paths = []
	try:
		if r7 >= 1:
			x = 0-3
			x = x-2
			paths.append(1)
		else:
			x = 3/x
			x = a9-9
			paths.append(2)
		if r7 > 3:
			x = 3-0
			a9 = a9*4
			paths.append(3)
		else:
			a9 = a9-8
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		r7 = a9**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))