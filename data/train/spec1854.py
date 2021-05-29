import numpy as np 

def function(x):

	a3 = x
	o1 = x
	paths = []
	try:
		if a3 >= 1:
			a3 = a3-8
			o1 = o1-4
			x = o1+4
			paths.append(1)
		else:
			a3 = 6-6
			x = x/6
			paths.append(2)
		if x <= 3:
			x = 9+2
			paths.append(3)
		else:
			x = x-x
			a3 = x+a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))