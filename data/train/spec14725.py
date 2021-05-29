import numpy as np 

def function(x):

	o5 = 7
	v5 = 5
	paths = []
	try:
		if v5 >= 0:
			o5 = o5-v5
			paths.append(1)
		else:
			x = v5*o5
			v5 = o5-9
			o5 = v5+x
			paths.append(2)
		if o5 >= 3:
			o5 = o5/v5
			x = 7-x
			v5 = 0-2
			paths.append(3)
		else:
			v5 = v5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))