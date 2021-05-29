import numpy as np 

def function(x):

	k2 = x
	f0 = x
	paths = []
	try:
		if f0 < 6:
			k2 = k2-3
			x = 5+4
			paths.append(1)
		else:
			f0 = f0/x
			x = f0+1
			paths.append(2)
		if f0 > 2:
			x = f0-x
			k2 = k2+6
			k2 = 7*x
			paths.append(3)
		else:
			x = x*f0
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))