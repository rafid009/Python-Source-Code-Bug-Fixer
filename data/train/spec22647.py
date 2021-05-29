import numpy as np 

def function(x):

	n9 = 7
	k9 = x
	x = 3
	paths = []
	try:
		if x > 9:
			k9 = n9*9
			k9 = 5/x
			paths.append(1)
		else:
			x = n9-x
			n9 = n9-8
			paths.append(2)
		if x <= 9:
			n9 = k9/n9
			x = x-3
			paths.append(3)
		else:
			k9 = k9+0
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