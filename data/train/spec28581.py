import numpy as np 

def function(x):

	o5 = 8
	x1 = x
	paths = []
	try:
		if x1 >= 3:
			o5 = o5/5
			o5 = o5*5
			o5 = o5/x
			paths.append(1)
		else:
			x = x1*1
			x1 = 8+3
			paths.append(2)
		if x1 > 8:
			x1 = o5-x1
			x = x1*x
			o5 = o5+x
			paths.append(3)
		else:
			o5 = o5*x
			x = x*3
			x = 6*o5
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