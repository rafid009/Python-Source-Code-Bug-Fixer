import numpy as np 

def function(x):

	n1 = 5
	v8 = 5
	x = 8
	paths = []
	try:
		if v8 < 7:
			v8 = v8+4
			paths.append(1)
		else:
			v8 = 4+v8
			v8 = 9+v8
			paths.append(2)
		if n1 > 7:
			n1 = n1/6
			n1 = n1*3
			n1 = 3-n1
			paths.append(3)
		else:
			n1 = 3/n1
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))