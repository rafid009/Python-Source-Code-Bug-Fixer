import numpy as np 

def function(x):

	v8 = 4
	c4 = 9
	paths = []
	try:
		if v8 > 7:
			x = 9/9
			x = 9-x
			v8 = v8+6
			paths.append(1)
		else:
			v8 = 3-v8
			v8 = x-5
			paths.append(2)
		if c4 >= 0:
			x = x/8
			paths.append(3)
		else:
			v8 = 6-v8
			v8 = 6+v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))