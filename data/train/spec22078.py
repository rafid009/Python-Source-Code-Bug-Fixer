import numpy as np 

def function(x):

	k0 = 9
	p3 = 5
	paths = []
	try:
		if k0 <= 7:
			p3 = 7*p3
			k0 = 2*k0
			k0 = x-k0
			paths.append(1)
		else:
			x = k0+x
			x = x/3
			paths.append(2)
		if k0 < 9:
			x = x+0
			k0 = 6*3
			p3 = k0-x
			paths.append(3)
		else:
			k0 = 9*7
			x = x*9
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