import numpy as np 

def function(x):

	k7 = x
	f7 = x
	paths = []
	try:
		if x < 9:
			k7 = k7+7
			x = 7/5
			f7 = x/4
			paths.append(1)
		else:
			k7 = k7+9
			k7 = k7/7
			paths.append(2)
		if x <= 9:
			f7 = f7+k7
			x = 9+f7
			f7 = f7+3
			paths.append(3)
		else:
			f7 = 4*f7
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