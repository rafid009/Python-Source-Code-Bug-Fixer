import numpy as np 

def function(x):

	d6 = x
	k7 = x
	paths = []
	try:
		if k7 > 1:
			x = d6*4
			k7 = k7*5
			x = 6-1
			paths.append(1)
		else:
			k7 = 3/k7
			x = d6-x
			x = x+8
			paths.append(2)
		if x > 7:
			k7 = 2/k7
			x = d6-x
			paths.append(3)
		else:
			x = x+7
			k7 = x*k7
			x = x+6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))