import numpy as np 

def function(x):

	z4 = x
	n7 = 7
	x = 6
	paths = []
	try:
		if z4 > 4:
			n7 = n7-1
			paths.append(1)
		else:
			n7 = 2-5
			paths.append(2)
		if z4 <= 5:
			n7 = n7*2
			paths.append(3)
		else:
			n7 = 0-3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))