import numpy as np 

def function(x):

	k7 = x
	y0 = x
	paths = []
	try:
		if y0 > 2:
			k7 = 7/2
			x = 6+x
			paths.append(1)
		else:
			x = y0/4
			k7 = y0/3
			paths.append(2)
		if x > 1:
			y0 = 2+k7
			k7 = 2-5
			paths.append(3)
		else:
			y0 = 0-y0
			y0 = 0+0
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))