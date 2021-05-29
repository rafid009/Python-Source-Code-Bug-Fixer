import numpy as np 

def function(x):

	v4 = x
	x7 = 1
	paths = []
	try:
		if v4 > 4:
			x = 3*3
			v4 = x7*v4
			v4 = x-v4
			paths.append(1)
		else:
			x7 = 2+5
			v4 = x+v4
			paths.append(2)
		if x > 3:
			v4 = v4-6
			paths.append(3)
		else:
			x7 = x7*x7
			v4 = 7-x7
			v4 = v4*x7
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