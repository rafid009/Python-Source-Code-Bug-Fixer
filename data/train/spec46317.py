import numpy as np 

def function(x):

	o7 = x
	f1 = x
	paths = []
	try:
		if x > 1:
			o7 = o7*1
			x = x-4
			paths.append(1)
		else:
			o7 = 6/o7
			o7 = 4+o7
			x = o7+7
			paths.append(2)
		if o7 > 8:
			f1 = f1-0
			f1 = o7-o7
			paths.append(3)
		else:
			x = 1-8
			f1 = f1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))