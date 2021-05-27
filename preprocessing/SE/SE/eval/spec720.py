import numpy as np 

def function(x):

	k0 = 0
	i3 = x
	paths = []
	try:
		if k0 > 9:
			i3 = 4*8
			i3 = i3+4
			k0 = 9-6
			paths.append(1)
		else:
			x = 9-x
			k0 = k0-i3
			paths.append(2)
		if k0 < 9:
			x = 4*x
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		k0 = i3**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))