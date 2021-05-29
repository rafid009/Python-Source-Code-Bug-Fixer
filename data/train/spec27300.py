import numpy as np 

def function(x):

	n8 = 1
	v8 = x
	paths = []
	try:
		if v8 >= 2:
			x = x/x
			paths.append(1)
		else:
			v8 = 3+v8
			x = v8/x
			v8 = v8/5
			paths.append(2)
		if v8 > 3:
			n8 = 0+n8
			paths.append(3)
		else:
			n8 = v8/n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))