import numpy as np 

def function(x):

	n7 = x
	j9 = 2
	paths = []
	try:
		if x < 9:
			n7 = n7-9
			x = 1/3
			paths.append(1)
		else:
			j9 = j9*3
			paths.append(2)
		if x <= 9:
			j9 = x+j9
			x = x+8
			j9 = 1*5
			paths.append(3)
		else:
			n7 = 7-5
			n7 = j9+5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))