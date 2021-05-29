import numpy as np 

def function(x):

	w3 = x
	o0 = 2
	paths = []
	try:
		if w3 > 4:
			w3 = o0+6
			paths.append(1)
		else:
			o0 = 9/9
			w3 = w3+x
			paths.append(2)
		if x > 4:
			o0 = o0*5
			x = x-0
			paths.append(3)
		else:
			w3 = w3*2
			o0 = x-w3
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