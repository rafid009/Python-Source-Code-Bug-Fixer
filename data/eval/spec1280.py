import numpy as np 

def function(x):

	k7 = 5
	u9 = 2
	paths = []
	try:
		if x > 0:
			u9 = u9-8
			paths.append(1)
		else:
			x = 9-x
			k7 = k7*8
			paths.append(2)
		if x >= 9:
			u9 = x*x
			k7 = 1*7
			paths.append(3)
		else:
			k7 = k7+8
			k7 = k7*x
			x = 6+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))