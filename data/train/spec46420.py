import numpy as np 

def function(x):

	k7 = 3
	v0 = 9
	paths = []
	try:
		if k7 >= 5:
			v0 = v0*1
			v0 = v0/1
			v0 = v0-9
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if v0 >= 6:
			v0 = 7-v0
			k7 = k7+4
			paths.append(3)
		else:
			x = x/k7
			x = x/v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))