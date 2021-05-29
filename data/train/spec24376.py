import numpy as np 

def function(x):

	j1 = 7
	n7 = x
	paths = []
	try:
		if n7 < 2:
			n7 = 3+n7
			paths.append(1)
		else:
			n7 = x+0
			j1 = 7*x
			paths.append(2)
		if j1 < 5:
			j1 = n7-8
			n7 = n7*1
			paths.append(3)
		else:
			x = 7-x
			x = x/x
			n7 = 9-j1
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