import numpy as np 

def function(x):

	j5 = x
	k0 = x
	x = x
	paths = []
	try:
		if x > 9:
			j5 = 7-j5
			k0 = k0+j5
			x = 7-x
			paths.append(1)
		else:
			k0 = 7-k0
			k0 = k0+1
			paths.append(2)
		if j5 < 9:
			j5 = x-8
			k0 = k0-4
			k0 = k0-0
			paths.append(3)
		else:
			j5 = j5*9
			k0 = k0*4
			k0 = k0/1
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