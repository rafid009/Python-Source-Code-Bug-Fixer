import numpy as np 

def function(x):

	n5 = x
	v4 = 9
	x = x
	paths = []
	try:
		if x >= 0:
			n5 = 2-n5
			paths.append(1)
		else:
			v4 = v4/1
			x = x*9
			paths.append(2)
		if n5 >= 9:
			v4 = v4+9
			x = 6-x
			paths.append(3)
		else:
			v4 = v4/6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))