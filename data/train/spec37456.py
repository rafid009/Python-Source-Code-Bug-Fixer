import numpy as np 

def function(x):

	w2 = x
	o0 = x
	paths = []
	try:
		if o0 >= 3:
			o0 = w2*o0
			paths.append(1)
		else:
			w2 = w2/3
			o0 = x+o0
			paths.append(2)
		if o0 >= 0:
			o0 = o0-7
			paths.append(3)
		else:
			o0 = 6+2
			o0 = x*0
			w2 = x-w2
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