import numpy as np 

def function(x):

	o0 = 6
	o5 = 1
	paths = []
	try:
		if x < 3:
			o0 = 9+o0
			x = x/9
			x = x*o0
			paths.append(1)
		else:
			x = x+o5
			o5 = o5+7
			paths.append(2)
		if o5 > 5:
			o5 = 2/o5
			o5 = o5*x
			paths.append(3)
		else:
			o0 = x-o0
			o0 = 5*o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))