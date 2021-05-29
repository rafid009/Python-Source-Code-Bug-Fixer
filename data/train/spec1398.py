import numpy as np 

def function(x):

	w3 = x
	o8 = 0
	paths = []
	try:
		if x >= 4:
			x = 5*x
			paths.append(1)
		else:
			w3 = 4+x
			paths.append(2)
		if o8 <= 7:
			w3 = w3-5
			o8 = 2*9
			paths.append(3)
		else:
			x = x+4
			o8 = 0-0
			w3 = w3*o8
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		o8 = w3**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))