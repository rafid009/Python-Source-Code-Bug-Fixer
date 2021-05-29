import numpy as np 

def function(x):

	v8 = x
	n4 = 7
	paths = []
	try:
		if x > 3:
			n4 = 8/v8
			v8 = v8/8
			paths.append(1)
		else:
			v8 = v8*1
			x = 5/x
			v8 = v8-7
			paths.append(2)
		if n4 >= 3:
			n4 = v8+5
			n4 = n4/1
			paths.append(3)
		else:
			n4 = 5*6
			n4 = 2+n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		v8 = n4**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))