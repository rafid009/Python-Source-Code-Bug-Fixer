import numpy as np 

def function(x):

	k0 = 1
	u5 = x
	paths = []
	try:
		if x <= 0:
			k0 = k0+7
			paths.append(1)
		else:
			u5 = k0*u5
			x = 4/x
			paths.append(2)
		if k0 < 9:
			u5 = 1*u5
			k0 = k0+9
			k0 = u5/9
			paths.append(3)
		else:
			k0 = 8/k0
			k0 = x+6
			x = 1*x
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