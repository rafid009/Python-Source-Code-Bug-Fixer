import numpy as np 

def function(x):

	o6 = 7
	w5 = x
	paths = []
	try:
		if x >= 3:
			w5 = w5*8
			o6 = o6*4
			x = x*x
			paths.append(1)
		else:
			w5 = w5+5
			o6 = o6+9
			paths.append(2)
		if w5 > 8:
			x = 4+w5
			w5 = w5-4
			o6 = 0/6
			paths.append(3)
		else:
			w5 = w5+o6
			x = x*x
			x = x*w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		o6 = w5**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))