import numpy as np 

def function(x):

	q0 = x
	k1 = 9
	paths = []
	try:
		if x <= 1:
			k1 = k1-1
			k1 = 5*4
			q0 = q0+3
			paths.append(1)
		else:
			k1 = 7*4
			paths.append(2)
		if k1 <= 7:
			q0 = 4-q0
			x = 5*x
			x = x/2
			paths.append(3)
		else:
			k1 = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))