import numpy as np 

def function(x):

	o6 = x
	e6 = 3
	x = x
	paths = []
	try:
		if o6 <= 8:
			o6 = e6*o6
			paths.append(1)
		else:
			e6 = e6-9
			e6 = e6+8
			paths.append(2)
		if e6 <= 0:
			o6 = o6+1
			e6 = 3+1
			paths.append(3)
		else:
			e6 = 8-o6
			o6 = o6*o6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))