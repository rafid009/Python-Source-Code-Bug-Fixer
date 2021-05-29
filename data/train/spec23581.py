import numpy as np 

def function(x):

	v8 = 6
	n8 = x
	paths = []
	try:
		if v8 > 0:
			v8 = v8*x
			n8 = 2/n8
			v8 = 1+7
			paths.append(1)
		else:
			n8 = n8-v8
			x = 4+x
			x = x/8
			paths.append(2)
		if v8 < 7:
			n8 = n8-x
			v8 = v8-v8
			n8 = n8-x
			paths.append(3)
		else:
			n8 = 4+n8
			x = v8/x
			n8 = n8-n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))