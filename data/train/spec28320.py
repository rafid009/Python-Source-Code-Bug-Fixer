import numpy as np 

def function(x):

	k0 = x
	i4 = 2
	x = x
	paths = []
	try:
		if i4 <= 1:
			k0 = 9-i4
			k0 = x/k0
			paths.append(1)
		else:
			i4 = i4+6
			i4 = k0/i4
			k0 = x-k0
			paths.append(2)
		if x > 3:
			i4 = x+x
			x = x-x
			paths.append(3)
		else:
			x = x+i4
			i4 = i4/5
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))