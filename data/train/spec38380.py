import numpy as np 

def function(x):

	a3 = 1
	o2 = x
	x = x
	paths = []
	try:
		if x > 3:
			a3 = 9-a3
			x = x+a3
			paths.append(1)
		else:
			a3 = o2-x
			o2 = o2/8
			paths.append(2)
		if a3 < 6:
			o2 = 5/4
			paths.append(3)
		else:
			o2 = 5+o2
			o2 = o2/x
			o2 = o2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))