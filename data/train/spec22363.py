import numpy as np 

def function(x):

	o8 = 3
	i3 = x
	paths = []
	try:
		if o8 < 8:
			i3 = i3*6
			i3 = 3+o8
			paths.append(1)
		else:
			i3 = 8*i3
			o8 = i3/9
			o8 = o8*6
			paths.append(2)
		if x <= 1:
			o8 = o8/o8
			paths.append(3)
		else:
			x = x-1
			x = o8/9
			o8 = x+o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))