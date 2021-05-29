import numpy as np 

def function(x):

	v2 = 4
	n3 = 1
	paths = []
	try:
		if n3 >= 4:
			x = 2/4
			n3 = 6/3
			paths.append(1)
		else:
			v2 = 3-9
			x = 6/x
			paths.append(2)
		if v2 < 3:
			n3 = n3/7
			n3 = v2+2
			paths.append(3)
		else:
			v2 = 6+v2
			v2 = v2/x
			v2 = x-v2
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))