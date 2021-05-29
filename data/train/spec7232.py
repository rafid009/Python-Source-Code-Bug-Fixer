import numpy as np 

def function(x):

	a6 = 5
	k1 = 9
	paths = []
	try:
		if k1 < 3:
			a6 = a6+5
			k1 = k1+8
			paths.append(1)
		else:
			k1 = x-4
			paths.append(2)
		if x >= 3:
			a6 = 6-a6
			k1 = k1/7
			paths.append(3)
		else:
			a6 = a6*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))