import numpy as np 

def function(x):

	o4 = x
	e7 = 9
	paths = []
	try:
		if e7 <= 2:
			x = o4/x
			o4 = o4*0
			paths.append(1)
		else:
			o4 = o4/5
			o4 = 2-o4
			x = e7*o4
			paths.append(2)
		if o4 <= 9:
			e7 = e7/2
			paths.append(3)
		else:
			o4 = o4*7
			o4 = o4-7
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