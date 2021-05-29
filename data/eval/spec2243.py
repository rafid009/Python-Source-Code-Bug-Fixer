import numpy as np 

def function(x):

	o1 = x
	a0 = 1
	x = 3
	paths = []
	try:
		if o1 < 4:
			x = 6*9
			paths.append(1)
		else:
			o1 = 9-2
			o1 = a0*9
			x = x-x
			paths.append(2)
		if o1 <= 9:
			o1 = 9/o1
			a0 = a0-5
			paths.append(3)
		else:
			a0 = a0-0
			o1 = a0*a0
			a0 = 9-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))