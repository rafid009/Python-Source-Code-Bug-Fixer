import numpy as np 

def function(x):

	i4 = x
	v8 = x
	paths = []
	try:
		if i4 >= 3:
			v8 = v8/7
			v8 = v8/8
			i4 = 2+v8
			paths.append(1)
		else:
			v8 = i4/3
			paths.append(2)
		if x >= 7:
			x = x/v8
			x = 1*v8
			x = 7/x
			paths.append(3)
		else:
			x = 9*x
			x = x/5
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))