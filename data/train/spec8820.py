import numpy as np 

def function(x):

	n7 = x
	u9 = 6
	paths = []
	try:
		if u9 > 1:
			u9 = u9/u9
			paths.append(1)
		else:
			n7 = x*x
			n7 = n7*8
			n7 = n7*n7
			paths.append(2)
		if n7 > 8:
			x = 1-9
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		u9 = n7**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))