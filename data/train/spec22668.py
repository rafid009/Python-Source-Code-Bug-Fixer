import numpy as np 

def function(x):

	k5 = 8
	n5 = x
	paths = []
	try:
		if n5 <= 1:
			k5 = 5*6
			n5 = n5*2
			paths.append(1)
		else:
			x = 2+k5
			n5 = k5*n5
			paths.append(2)
		if n5 <= 6:
			x = x+1
			k5 = 9+3
			paths.append(3)
		else:
			k5 = 7-2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		k5 = n5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))