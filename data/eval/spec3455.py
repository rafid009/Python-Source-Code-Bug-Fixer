import numpy as np 

def function(x):

	k0 = 7
	n9 = 1
	paths = []
	try:
		if n9 <= 6:
			k0 = k0*4
			paths.append(1)
		else:
			x = n9/6
			n9 = 4/n9
			x = x/6
			paths.append(2)
		if x > 0:
			n9 = x-n9
			n9 = 3/7
			paths.append(3)
		else:
			k0 = 1+k0
			n9 = n9*2
			k0 = k0+4
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