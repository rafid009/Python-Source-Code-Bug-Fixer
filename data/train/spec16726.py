import numpy as np 

def function(x):

	v4 = x
	k0 = 7
	paths = []
	try:
		if v4 < 5:
			x = v4+x
			k0 = k0+k0
			paths.append(1)
		else:
			v4 = 0/8
			x = x+8
			x = k0-0
			paths.append(2)
		if k0 > 4:
			k0 = 3/k0
			v4 = 4-v4
			k0 = k0-k0
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))