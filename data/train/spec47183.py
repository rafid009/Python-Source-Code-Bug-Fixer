import numpy as np 

def function(x):

	a0 = 2
	k6 = 3
	paths = []
	try:
		if k6 < 1:
			x = x+9
			x = x-2
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x >= 3:
			a0 = a0-k6
			paths.append(3)
		else:
			x = x/7
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