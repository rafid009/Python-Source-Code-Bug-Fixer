import numpy as np 

def function(x):

	k7 = x
	x6 = x
	paths = []
	try:
		if x >= 8:
			x6 = x6+k7
			k7 = k7+6
			paths.append(1)
		else:
			x6 = x6*x6
			x = 5/x
			paths.append(2)
		if x6 <= 3:
			x6 = x6*1
			k7 = 5+k7
			paths.append(3)
		else:
			k7 = k7*k7
			x = x-9
			k7 = k7-5
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