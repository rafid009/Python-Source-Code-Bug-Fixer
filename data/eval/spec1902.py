import numpy as np 

def function(x):

	x3 = x
	o5 = x
	paths = []
	try:
		if o5 < 1:
			o5 = o5*2
			paths.append(1)
		else:
			x3 = o5-5
			paths.append(2)
		if o5 > 2:
			o5 = x-o5
			o5 = o5-6
			paths.append(3)
		else:
			x3 = x3*0
			x = 5*2
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))