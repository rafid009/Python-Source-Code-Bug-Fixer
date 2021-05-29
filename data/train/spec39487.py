import numpy as np 

def function(x):

	a9 = x
	d1 = x
	paths = []
	try:
		if x < 0:
			d1 = d1-7
			paths.append(1)
		else:
			a9 = 4-a9
			paths.append(2)
		if a9 < 2:
			d1 = a9*4
			a9 = x-d1
			d1 = 9/d1
			paths.append(3)
		else:
			d1 = d1-6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))