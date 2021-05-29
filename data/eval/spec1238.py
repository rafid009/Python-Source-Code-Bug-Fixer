import numpy as np 

def function(x):

	k2 = x
	y3 = 7
	paths = []
	try:
		if y3 > 3:
			x = x*k2
			paths.append(1)
		else:
			k2 = 7-x
			x = 0-x
			paths.append(2)
		if x >= 0:
			x = y3+x
			x = x*1
			y3 = 9+y3
			paths.append(3)
		else:
			k2 = 4*k2
			k2 = 0+3
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))