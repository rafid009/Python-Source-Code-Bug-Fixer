import numpy as np 

def function(x):

	k0 = x
	j3 = 7
	paths = []
	try:
		if j3 <= 3:
			x = 2/x
			x = 8-x
			j3 = j3/2
			paths.append(1)
		else:
			j3 = j3/1
			paths.append(2)
		if x >= 6:
			x = 9/x
			j3 = x/x
			paths.append(3)
		else:
			j3 = j3-2
			x = x-2
			j3 = j3+8
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