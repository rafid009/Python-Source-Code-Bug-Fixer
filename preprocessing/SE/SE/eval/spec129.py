import numpy as np 

def function(x):

	o4 = x
	o2 = x
	paths = []
	try:
		if o2 > 5:
			x = 9/2
			paths.append(1)
		else:
			o2 = x/2
			paths.append(2)
		if x < 9:
			o2 = 6/5
			o2 = o4-o2
			paths.append(3)
		else:
			o2 = o2+o2
			o4 = 2/o2
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))