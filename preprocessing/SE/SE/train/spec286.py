import numpy as np 

def function(x):

	o0 = x
	w3 = 2
	x = x
	paths = []
	try:
		if o0 > 4:
			x = 1+x
			o0 = 9-o0
			paths.append(1)
		else:
			w3 = w3*3
			paths.append(2)
		if w3 >= 3:
			x = 0*o0
			o0 = o0+x
			x = x/o0
			paths.append(3)
		else:
			w3 = 4+w3
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		w3 = o0**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))