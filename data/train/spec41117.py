import numpy as np 

def function(x):

	b7 = x
	o6 = 1
	paths = []
	try:
		if x > 5:
			o6 = 8+7
			paths.append(1)
		else:
			b7 = o6-1
			paths.append(2)
		if o6 <= 3:
			o6 = 2/o6
			o6 = 6-8
			paths.append(3)
		else:
			o6 = b7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))