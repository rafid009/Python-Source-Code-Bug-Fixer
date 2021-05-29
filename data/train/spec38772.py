import numpy as np 

def function(x):

	o6 = x
	a6 = 2
	paths = []
	try:
		if a6 > 8:
			o6 = o6/1
			o6 = o6/6
			paths.append(1)
		else:
			x = o6/5
			o6 = o6-o6
			o6 = o6*3
			paths.append(2)
		if a6 > 5:
			a6 = a6-2
			o6 = o6*1
			x = 4+0
			paths.append(3)
		else:
			o6 = o6/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))