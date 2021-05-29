import numpy as np 

def function(x):

	o6 = 0
	x9 = x
	paths = []
	try:
		if x < 5:
			o6 = o6*7
			o6 = x9*2
			o6 = 0*8
			paths.append(1)
		else:
			x9 = x9*o6
			x9 = 9*x9
			x = x+6
			paths.append(2)
		if o6 > 8:
			x = x+2
			x = 4/x
			paths.append(3)
		else:
			x = x/5
			o6 = 3+o6
			x9 = x9-6
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		o6 = x9**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))