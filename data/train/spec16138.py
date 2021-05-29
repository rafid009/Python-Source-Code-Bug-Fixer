import numpy as np 

def function(x):

	v3 = x
	n4 = 5
	x = x
	paths = []
	try:
		if n4 > 9:
			x = n4-x
			n4 = x/3
			x = 0-x
			paths.append(1)
		else:
			n4 = n4-9
			x = n4+x
			v3 = 3*v3
			paths.append(2)
		if n4 <= 1:
			v3 = v3*9
			x = 9-n4
			paths.append(3)
		else:
			v3 = x/v3
			x = x*3
			v3 = 8*v3
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))