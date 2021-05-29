import numpy as np 

def function(x):

	k1 = x
	e2 = x
	paths = []
	try:
		if x > 4:
			k1 = 3-k1
			paths.append(1)
		else:
			x = x*x
			e2 = 1+e2
			x = x*5
			paths.append(2)
		if x <= 2:
			e2 = e2+6
			k1 = 0*7
			paths.append(3)
		else:
			k1 = e2*k1
			e2 = e2*7
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		k1 = e2**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))