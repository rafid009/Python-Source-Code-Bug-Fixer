import numpy as np 

def function(x):

	k1 = x
	e6 = x
	paths = []
	try:
		if e6 > 2:
			k1 = k1+3
			paths.append(1)
		else:
			x = x-1
			e6 = x/4
			x = x+7
			paths.append(2)
		if e6 >= 7:
			x = 7/x
			x = 4-x
			paths.append(3)
		else:
			x = x*8
			x = 4/e6
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))