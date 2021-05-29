import numpy as np 

def function(x):

	e8 = x
	o6 = x
	paths = []
	try:
		if o6 < 7:
			x = x+o6
			o6 = o6+6
			o6 = x+6
			paths.append(1)
		else:
			e8 = 5*e8
			paths.append(2)
		if e8 > 8:
			e8 = o6+7
			o6 = o6*o6
			o6 = 3+o6
			paths.append(3)
		else:
			e8 = 8-e8
			x = x-o6
			x = x-5
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		e8 = o6**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))