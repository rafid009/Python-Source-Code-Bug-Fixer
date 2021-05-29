import numpy as np 

def function(x):

	k0 = x
	e4 = 4
	paths = []
	try:
		if e4 > 1:
			k0 = k0+x
			x = x+2
			e4 = 3-9
			paths.append(1)
		else:
			k0 = k0+7
			x = 7+x
			k0 = 1+k0
			paths.append(2)
		if e4 <= 4:
			e4 = 3/7
			paths.append(3)
		else:
			k0 = 7*k0
			x = 7-e4
			x = x-1
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