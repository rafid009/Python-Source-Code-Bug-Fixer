import numpy as np 

def function(x):

	n9 = x
	n7 = 3
	paths = []
	try:
		if n9 <= 8:
			n9 = n9*n9
			n9 = n7*n9
			n9 = n9*x
			paths.append(1)
		else:
			x = n7+x
			n9 = n9*1
			paths.append(2)
		if n9 > 1:
			n9 = n7-2
			n9 = 2/n9
			x = x+8
			paths.append(3)
		else:
			x = 1+3
			n9 = n9-9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))