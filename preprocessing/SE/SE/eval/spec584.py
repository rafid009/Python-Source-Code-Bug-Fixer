import numpy as np 

def function(x):

	m2 = 6
	k7 = x
	paths = []
	try:
		if k7 < 6:
			x = 2-x
			paths.append(1)
		else:
			k7 = k7*9
			k7 = k7*k7
			paths.append(2)
		if k7 <= 1:
			k7 = 2/m2
			k7 = k7-m2
			paths.append(3)
		else:
			k7 = k7*m2
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