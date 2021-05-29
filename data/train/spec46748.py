import numpy as np 

def function(x):

	o5 = 9
	w2 = x
	paths = []
	try:
		if o5 < 1:
			o5 = 9-2
			w2 = 4/7
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if w2 >= 1:
			x = x-9
			w2 = o5/4
			w2 = w2/6
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))