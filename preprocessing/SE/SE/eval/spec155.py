import numpy as np 

def function(x):

	o5 = 3
	j5 = 1
	paths = []
	try:
		if j5 < 2:
			j5 = j5-1
			j5 = j5/o5
			paths.append(1)
		else:
			o5 = o5+j5
			paths.append(2)
		if x >= 9:
			o5 = o5+6
			paths.append(3)
		else:
			o5 = o5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))