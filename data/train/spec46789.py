import numpy as np 

def function(x):

	w9 = x
	o2 = 7
	paths = []
	try:
		if o2 < 1:
			o2 = o2/8
			paths.append(1)
		else:
			o2 = 4+x
			w9 = w9-9
			o2 = x-x
			paths.append(2)
		if x <= 1:
			x = x/w9
			w9 = w9*4
			x = w9*7
			paths.append(3)
		else:
			o2 = w9-o2
			w9 = w9*7
			o2 = o2*x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))