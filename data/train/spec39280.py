import numpy as np 

def function(x):

	k7 = x
	f8 = x
	paths = []
	try:
		if k7 > 4:
			f8 = 2+f8
			k7 = k7+8
			f8 = 9-f8
			paths.append(1)
		else:
			x = 9*5
			f8 = f8*f8
			x = 2/4
			paths.append(2)
		if x >= 2:
			x = k7-x
			paths.append(3)
		else:
			k7 = k7+3
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		k7 = f8**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))