import numpy as np 

def function(x):

	q9 = 0
	k0 = x
	paths = []
	try:
		if x > 2:
			x = 2+1
			paths.append(1)
		else:
			x = x+k0
			x = 3+9
			q9 = q9-5
			paths.append(2)
		if k0 > 7:
			x = x+x
			k0 = k0-5
			k0 = k0-6
			paths.append(3)
		else:
			q9 = q9*x
			x = k0*x
			x = q9+x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))