import numpy as np 

def function(x):

	w6 = x
	o5 = x
	paths = []
	try:
		if w6 < 0:
			o5 = 6+o5
			o5 = 3+o5
			paths.append(1)
		else:
			w6 = o5-o5
			w6 = w6+x
			x = x*x
			paths.append(2)
		if w6 >= 7:
			x = 8-4
			x = x-2
			paths.append(3)
		else:
			o5 = x/o5
			w6 = 4-o5
			x = x*x
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