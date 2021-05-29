import numpy as np 

def function(x):

	k1 = 1
	l7 = 4
	paths = []
	try:
		if x > 6:
			x = x*x
			paths.append(1)
		else:
			k1 = k1/1
			x = x/5
			x = x-9
			paths.append(2)
		if x >= 5:
			l7 = 9/l7
			k1 = l7-k1
			paths.append(3)
		else:
			l7 = l7+7
			k1 = 0/k1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))