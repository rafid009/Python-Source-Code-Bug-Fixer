import numpy as np 

def function(x):

	i3 = x
	o6 = 2
	paths = []
	try:
		if o6 <= 8:
			o6 = o6*o6
			paths.append(1)
		else:
			o6 = 4/o6
			i3 = i3+6
			paths.append(2)
		if i3 < 1:
			x = x/6
			paths.append(3)
		else:
			i3 = i3+o6
			i3 = o6/i3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))