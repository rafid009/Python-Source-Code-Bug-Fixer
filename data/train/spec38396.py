import numpy as np 

def function(x):

	f9 = 9
	k0 = x
	paths = []
	try:
		if x < 7:
			f9 = f9-0
			paths.append(1)
		else:
			f9 = f9*x
			f9 = f9-3
			x = 1-k0
			paths.append(2)
		if x >= 9:
			x = 4+2
			x = 6/x
			paths.append(3)
		else:
			k0 = k0*x
			k0 = k0+5
			k0 = k0*5
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		f9 = k0**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))