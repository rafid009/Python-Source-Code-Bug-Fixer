import numpy as np 

def function(x):

	r4 = x
	k7 = x
	paths = []
	try:
		if k7 > 7:
			x = x-4
			k7 = k7-r4
			paths.append(1)
		else:
			r4 = r4*x
			paths.append(2)
		if k7 < 6:
			r4 = 1-r4
			k7 = x-5
			paths.append(3)
		else:
			r4 = r4+9
			r4 = r4+3
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