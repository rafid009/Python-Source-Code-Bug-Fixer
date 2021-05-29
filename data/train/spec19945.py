import numpy as np 

def function(x):

	o2 = x
	x3 = 6
	x = x
	paths = []
	try:
		if x3 > 2:
			x = 4-o2
			x = x+x
			x3 = x3+0
			paths.append(1)
		else:
			o2 = 5+o2
			x = 5-x
			paths.append(2)
		if x3 > 1:
			o2 = 1/o2
			x3 = x3/o2
			paths.append(3)
		else:
			x = x-0
			o2 = o2*2
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))