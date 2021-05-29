import numpy as np 

def function(x):

	n9 = x
	k5 = 3
	paths = []
	try:
		if k5 > 6:
			x = x-n9
			paths.append(1)
		else:
			x = k5/n9
			paths.append(2)
		if n9 < 3:
			k5 = k5-3
			x = n9/x
			paths.append(3)
		else:
			n9 = n9/9
			k5 = x+k5
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		k5 = n9**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))