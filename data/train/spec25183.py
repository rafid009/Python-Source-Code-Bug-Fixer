import numpy as np 

def function(x):

	k0 = x
	a4 = 2
	paths = []
	try:
		if k0 <= 6:
			a4 = 6+7
			paths.append(1)
		else:
			x = 0+x
			a4 = 3/4
			a4 = a4/2
			paths.append(2)
		if k0 <= 1:
			a4 = a4+8
			x = 0*3
			paths.append(3)
		else:
			a4 = a4-1
			k0 = 6*a4
			x = x+a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		k0 = a4**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))