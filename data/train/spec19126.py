import numpy as np 

def function(x):

	o5 = 7
	h1 = 3
	paths = []
	try:
		if x > 8:
			h1 = 0-h1
			h1 = h1+0
			paths.append(1)
		else:
			o5 = x+1
			paths.append(2)
		if o5 < 0:
			o5 = o5-o5
			o5 = o5-6
			paths.append(3)
		else:
			o5 = 3+o5
			o5 = 2-o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))