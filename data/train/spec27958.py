import numpy as np 

def function(x):

	e3 = 5
	v4 = 8
	paths = []
	try:
		if e3 >= 8:
			v4 = 4+x
			paths.append(1)
		else:
			v4 = v4/e3
			v4 = v4*x
			paths.append(2)
		if x > 1:
			e3 = e3*9
			e3 = 7/e3
			e3 = e3*3
			paths.append(3)
		else:
			x = x+9
			x = 9*x
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