import numpy as np 

def function(x):

	r6 = 3
	k5 = 7
	paths = []
	try:
		if r6 <= 2:
			k5 = k5/2
			x = 3-x
			k5 = x-6
			paths.append(1)
		else:
			r6 = r6*k5
			r6 = x*r6
			paths.append(2)
		if x >= 8:
			x = x-5
			k5 = k5-1
			k5 = 3/k5
			paths.append(3)
		else:
			r6 = k5/r6
			r6 = 3*r6
			x = r6*x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))