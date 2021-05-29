import numpy as np 

def function(x):

	e1 = x
	o1 = 4
	paths = []
	try:
		if x >= 3:
			x = x-7
			o1 = 4*o1
			paths.append(1)
		else:
			e1 = e1/3
			o1 = o1/x
			x = o1-x
			paths.append(2)
		if o1 <= 2:
			e1 = e1/8
			o1 = o1-6
			e1 = e1+5
			paths.append(3)
		else:
			e1 = 8-o1
			x = x*3
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))