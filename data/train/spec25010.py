import numpy as np 

def function(x):

	o0 = x
	e8 = x
	paths = []
	try:
		if o0 >= 4:
			o0 = o0-4
			paths.append(1)
		else:
			o0 = x-3
			paths.append(2)
		if e8 >= 4:
			x = 6-0
			x = 9-o0
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		o0 = e8**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))