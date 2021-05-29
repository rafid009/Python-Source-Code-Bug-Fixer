import numpy as np 

def function(x):

	a1 = x
	k0 = x
	paths = []
	try:
		if a1 >= 7:
			x = x+k0
			a1 = a1/x
			x = x/5
			paths.append(1)
		else:
			x = 7*x
			k0 = k0/1
			x = x*x
			paths.append(2)
		if x < 7:
			a1 = a1*a1
			x = x+k0
			x = a1-x
			paths.append(3)
		else:
			k0 = k0*a1
			k0 = a1*k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))