import numpy as np 

def function(x):

	t9 = x
	k0 = 9
	paths = []
	try:
		if k0 >= 4:
			k0 = k0-2
			paths.append(1)
		else:
			x = 1*x
			x = x*x
			paths.append(2)
		if x < 9:
			k0 = k0+k0
			k0 = k0+7
			k0 = 2*k0
			paths.append(3)
		else:
			k0 = 9-k0
			x = k0/t9
			x = t9*5
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		k0 = t9**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))