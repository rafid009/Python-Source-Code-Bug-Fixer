import numpy as np 

def function(x):

	a0 = 8
	k5 = 6
	paths = []
	try:
		if k5 > 5:
			a0 = 9-a0
			k5 = x*6
			x = 1/3
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if x <= 7:
			x = 1+a0
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		a0 = k5**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))