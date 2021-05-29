import numpy as np 

def function(x):

	l9 = 3
	k0 = x
	paths = []
	try:
		if l9 > 7:
			k0 = 5-k0
			paths.append(1)
		else:
			l9 = l9+2
			l9 = 1*4
			k0 = x*k0
			paths.append(2)
		if x < 3:
			l9 = k0*l9
			l9 = k0*l9
			k0 = k0+7
			paths.append(3)
		else:
			x = l9*x
			x = 4-x
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