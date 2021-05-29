import numpy as np 

def function(x):

	e6 = x
	v4 = x
	paths = []
	try:
		if v4 > 4:
			e6 = e6*9
			paths.append(1)
		else:
			x = x/1
			e6 = x*e6
			paths.append(2)
		if x >= 3:
			e6 = x+4
			e6 = e6*3
			v4 = e6/e6
			paths.append(3)
		else:
			v4 = 5/v4
			v4 = v4*9
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