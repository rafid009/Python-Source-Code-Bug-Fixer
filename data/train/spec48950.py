import numpy as np 

def function(x):

	v8 = x
	n6 = x
	paths = []
	try:
		if v8 >= 4:
			x = 0*x
			x = 1-x
			x = x/2
			paths.append(1)
		else:
			v8 = n6*2
			v8 = v8-v8
			paths.append(2)
		if v8 >= 1:
			n6 = n6/x
			v8 = 5+x
			x = v8-7
			paths.append(3)
		else:
			n6 = n6*3
			x = x-x
			v8 = x+8
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		v8 = n6**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))