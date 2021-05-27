import numpy as np 

def function(x):

	a4 = x
	k1 = x
	x = 7
	paths = []
	try:
		if x >= 5:
			a4 = 5-a4
			paths.append(1)
		else:
			k1 = a4*x
			k1 = x/x
			paths.append(2)
		if a4 > 2:
			k1 = k1-8
			a4 = 1*5
			paths.append(3)
		else:
			a4 = x+4
			x = x-5
			a4 = a4/9
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))