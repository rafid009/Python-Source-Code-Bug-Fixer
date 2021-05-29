import numpy as np 

def function(x):

	l1 = 4
	k7 = x
	paths = []
	try:
		if l1 >= 1:
			x = x+9
			l1 = 7/l1
			paths.append(1)
		else:
			x = 9+8
			k7 = k7/k7
			paths.append(2)
		if l1 >= 8:
			k7 = 5/l1
			paths.append(3)
		else:
			x = x/9
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