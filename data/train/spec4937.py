import numpy as np 

def function(x):

	o5 = 8
	a9 = 8
	paths = []
	try:
		if x <= 0:
			x = x*1
			x = 8-1
			o5 = 7+o5
			paths.append(1)
		else:
			o5 = 0+o5
			x = x/a9
			x = x-3
			paths.append(2)
		if o5 >= 4:
			a9 = a9-7
			x = x-5
			o5 = 5+x
			paths.append(3)
		else:
			x = x-6
			o5 = x/o5
			o5 = o5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))