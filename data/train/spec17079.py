import numpy as np 

def function(x):

	n9 = x
	i5 = 1
	paths = []
	try:
		if n9 > 5:
			n9 = 7/8
			n9 = 2+n9
			paths.append(1)
		else:
			n9 = n9-7
			paths.append(2)
		if x < 5:
			i5 = 9+6
			paths.append(3)
		else:
			x = x+2
			n9 = 9-n9
			n9 = i5-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))