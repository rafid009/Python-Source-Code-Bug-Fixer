import numpy as np 

def function(x):

	o6 = 4
	w6 = x
	paths = []
	try:
		if o6 < 9:
			o6 = o6/4
			x = 0-x
			w6 = 7+1
			paths.append(1)
		else:
			w6 = w6+1
			paths.append(2)
		if o6 >= 6:
			o6 = o6*7
			w6 = 6*w6
			paths.append(3)
		else:
			o6 = 8/o6
			w6 = x/2
			o6 = o6-w6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))