import numpy as np 

def function(x):

	v3 = x
	o4 = 6
	paths = []
	try:
		if v3 <= 9:
			x = x-1
			paths.append(1)
		else:
			o4 = 0+o4
			x = v3-x
			paths.append(2)
		if o4 < 1:
			o4 = 0+o4
			paths.append(3)
		else:
			o4 = 6/o4
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		o4 = v3**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))