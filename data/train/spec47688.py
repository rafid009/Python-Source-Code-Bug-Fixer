import numpy as np 

def function(x):

	b2 = 7
	k0 = 6
	paths = []
	try:
		if x > 1:
			x = x+7
			x = x-1
			paths.append(1)
		else:
			b2 = 1+b2
			b2 = b2*b2
			k0 = 1/k0
			paths.append(2)
		if k0 > 2:
			k0 = 4-k0
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))