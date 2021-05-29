import numpy as np 

def function(x):

	x5 = x
	k0 = x
	paths = []
	try:
		if x5 > 7:
			x5 = x5-9
			x = x5+9
			paths.append(1)
		else:
			x5 = 6-x5
			x = x-8
			paths.append(2)
		if x >= 8:
			k0 = x+x
			x = x*0
			x = k0-0
			paths.append(3)
		else:
			x = 3*x
			x = x*k0
			x5 = x5+x
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