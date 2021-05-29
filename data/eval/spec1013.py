import numpy as np 

def function(x):

	o6 = x
	e9 = 0
	paths = []
	try:
		if o6 >= 8:
			o6 = 9/7
			x = x/x
			paths.append(1)
		else:
			o6 = x*8
			o6 = o6*o6
			paths.append(2)
		if o6 < 3:
			x = e9+x
			o6 = 7*o6
			x = e9-4
			paths.append(3)
		else:
			o6 = x/2
			o6 = o6*e9
			e9 = 5+x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))