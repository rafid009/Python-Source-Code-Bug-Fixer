import numpy as np 

def function(x):

	k7 = 8
	a6 = x
	paths = []
	try:
		if k7 > 1:
			k7 = 9-1
			x = 6-k7
			paths.append(1)
		else:
			a6 = k7-a6
			k7 = a6*k7
			paths.append(2)
		if x >= 0:
			k7 = 7/4
			x = k7*3
			a6 = a6/5
			paths.append(3)
		else:
			k7 = x/3
			a6 = x*a6
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		a6 = k7**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))