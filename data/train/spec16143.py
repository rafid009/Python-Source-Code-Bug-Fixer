import numpy as np 

def function(x):

	q7 = 7
	k7 = 1
	paths = []
	try:
		if x >= 1:
			x = x/8
			x = 9-x
			q7 = 8/k7
			paths.append(1)
		else:
			x = x*3
			q7 = q7-0
			paths.append(2)
		if x <= 8:
			q7 = 4*q7
			k7 = x/1
			paths.append(3)
		else:
			q7 = q7*1
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