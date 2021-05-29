import numpy as np 

def function(x):

	u7 = x
	n7 = x
	paths = []
	try:
		if n7 > 6:
			n7 = u7/n7
			u7 = u7-0
			paths.append(1)
		else:
			n7 = n7*5
			x = 8*9
			n7 = n7*9
			paths.append(2)
		if n7 <= 9:
			n7 = n7-8
			paths.append(3)
		else:
			x = 4/x
			n7 = n7*x
			x = x/8
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		u7 = n7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))