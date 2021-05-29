import numpy as np 

def function(x):

	k5 = 6
	v6 = 5
	paths = []
	try:
		if v6 <= 2:
			v6 = 8-4
			paths.append(1)
		else:
			k5 = x-v6
			k5 = x+k5
			v6 = k5+3
			paths.append(2)
		if v6 < 9:
			v6 = 8-v6
			x = x/2
			v6 = v6+k5
			paths.append(3)
		else:
			k5 = 8*v6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))