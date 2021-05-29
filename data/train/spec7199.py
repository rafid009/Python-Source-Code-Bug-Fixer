import numpy as np 

def function(x):

	a9 = 3
	r4 = x
	paths = []
	try:
		if r4 >= 2:
			r4 = r4-a9
			paths.append(1)
		else:
			x = x-6
			r4 = 2*9
			r4 = r4-7
			paths.append(2)
		if a9 >= 6:
			r4 = r4*r4
			a9 = 0*7
			paths.append(3)
		else:
			a9 = a9-x
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