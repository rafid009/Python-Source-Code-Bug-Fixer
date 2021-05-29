import numpy as np 

def function(x):

	v8 = x
	o9 = x
	paths = []
	try:
		if v8 >= 9:
			v8 = v8/x
			x = 7/x
			x = 0-x
			paths.append(1)
		else:
			v8 = v8/5
			v8 = 2+v8
			x = 1-x
			paths.append(2)
		if x > 1:
			v8 = x/v8
			x = x/8
			paths.append(3)
		else:
			o9 = 0/o9
			o9 = v8/9
			v8 = 7+3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))