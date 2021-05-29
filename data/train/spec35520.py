import numpy as np 

def function(x):

	v4 = 6
	paths = []
	try:
		if v4 >= 0:
			v4 = v4+v4
			v4 = v4/8
			paths.append(1)
		else:
			v4 = 5+v4
			v4 = 9*8
			v4 = v4+0
			paths.append(2)
		if x < 5:
			x = 1+x
			x = 6/1
			v4 = x-8
			paths.append(3)
		else:
			v4 = x/v4
			x = v4-x
			x = x/v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))