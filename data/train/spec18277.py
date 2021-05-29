import numpy as np 

def function(x):

	n2 = 4
	u7 = 5
	paths = []
	try:
		if n2 < 9:
			n2 = n2-0
			u7 = 1-n2
			u7 = x/u7
			paths.append(1)
		else:
			u7 = 4*7
			n2 = u7+u7
			n2 = n2*8
			paths.append(2)
		if n2 < 6:
			x = 5-x
			paths.append(3)
		else:
			x = x/2
			n2 = u7*n2
			n2 = x+u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))