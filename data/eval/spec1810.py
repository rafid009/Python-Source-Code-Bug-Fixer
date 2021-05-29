import numpy as np 

def function(x):

	a2 = x
	x4 = 4
	paths = []
	try:
		if x <= 3:
			x4 = x4-8
			paths.append(1)
		else:
			a2 = 6*a2
			x = x*6
			x4 = 0-x4
			paths.append(2)
		if x4 <= 4:
			x4 = x+9
			paths.append(3)
		else:
			x = x-x4
			x = x+0
			x = 2*x4
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x4 = a2**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))