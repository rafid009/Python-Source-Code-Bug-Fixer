import numpy as np 

def function(x):

	o6 = x
	w4 = x
	paths = []
	try:
		if w4 > 5:
			o6 = x/4
			paths.append(1)
		else:
			o6 = o6+x
			x = 7/o6
			paths.append(2)
		if x <= 2:
			x = 2/2
			x = 3-x
			x = 4-9
			paths.append(3)
		else:
			x = 6*x
			o6 = 3+o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))