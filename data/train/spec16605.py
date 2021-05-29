import numpy as np 

def function(x):

	w9 = 0
	o5 = x
	paths = []
	try:
		if x >= 6:
			o5 = o5-o5
			o5 = w9-4
			w9 = w9/4
			paths.append(1)
		else:
			w9 = w9+7
			o5 = o5-3
			w9 = o5*w9
			paths.append(2)
		if o5 >= 0:
			x = 8-2
			x = w9-1
			w9 = o5*x
			paths.append(3)
		else:
			o5 = 8*8
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		o5 = w9**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))