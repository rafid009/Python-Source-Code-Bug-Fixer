import numpy as np 

def function(x):

	f4 = x
	o5 = x
	paths = []
	try:
		if o5 >= 6:
			x = f4-6
			paths.append(1)
		else:
			f4 = x+o5
			paths.append(2)
		if o5 <= 1:
			f4 = f4-1
			paths.append(3)
		else:
			o5 = o5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))