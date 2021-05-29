import numpy as np 

def function(x):

	k1 = 7
	u1 = x
	paths = []
	try:
		if k1 > 8:
			x = x*x
			u1 = u1*u1
			paths.append(1)
		else:
			u1 = 2*k1
			paths.append(2)
		if x < 2:
			k1 = x*2
			u1 = 2-4
			paths.append(3)
		else:
			k1 = 6+7
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