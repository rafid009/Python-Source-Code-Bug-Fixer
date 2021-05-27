import numpy as np 

def function(x):

	o5 = x
	j9 = 9
	x = 0
	paths = []
	try:
		if o5 <= 5:
			j9 = x/j9
			j9 = j9/1
			x = x+j9
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x <= 8:
			j9 = 4-o5
			j9 = j9*6
			paths.append(3)
		else:
			o5 = o5+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))