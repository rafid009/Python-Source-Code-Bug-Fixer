import numpy as np 

def function(x):

	x8 = x
	k7 = 4
	paths = []
	try:
		if x <= 3:
			x = 9/x
			paths.append(1)
		else:
			x8 = x*0
			k7 = 9*8
			k7 = x-7
			paths.append(2)
		if x8 > 9:
			x8 = x8*x8
			x = 5/k7
			k7 = k7/k7
			paths.append(3)
		else:
			k7 = 7+x
			k7 = k7-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))