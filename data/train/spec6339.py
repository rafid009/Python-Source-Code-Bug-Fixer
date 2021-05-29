import numpy as np 

def function(x):

	n9 = 3
	v9 = 8
	paths = []
	try:
		if x >= 5:
			n9 = 4+n9
			n9 = n9-x
			paths.append(1)
		else:
			n9 = 0+n9
			x = 5/9
			paths.append(2)
		if v9 >= 3:
			v9 = v9-n9
			v9 = v9*v9
			paths.append(3)
		else:
			v9 = v9+9
			n9 = 2-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		v9 = n9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))