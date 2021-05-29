import numpy as np 

def function(x):

	e1 = x
	o5 = x
	paths = []
	try:
		if o5 >= 6:
			e1 = e1+e1
			x = 0/x
			o5 = o5+5
			paths.append(1)
		else:
			x = 8+8
			e1 = 0+9
			e1 = x-6
			paths.append(2)
		if x <= 6:
			e1 = 2+6
			e1 = e1+e1
			paths.append(3)
		else:
			o5 = 0/o5
			x = x-2
			e1 = 8-e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))