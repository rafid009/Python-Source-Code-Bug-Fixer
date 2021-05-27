import numpy as np 

def function(x):

	o1 = 9
	a2 = x
	paths = []
	try:
		if o1 <= 2:
			a2 = 6+o1
			paths.append(1)
		else:
			o1 = a2+o1
			o1 = 8/o1
			x = 9-0
			paths.append(2)
		if a2 > 0:
			x = x-0
			a2 = a2/x
			a2 = a2*a2
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))