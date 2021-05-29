import numpy as np 

def function(x):

	k5 = x
	e1 = 8
	paths = []
	try:
		if e1 <= 2:
			e1 = x*e1
			x = e1-7
			k5 = 7/x
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if k5 < 5:
			e1 = e1*9
			paths.append(3)
		else:
			x = x-e1
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))