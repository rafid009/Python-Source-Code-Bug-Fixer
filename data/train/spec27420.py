import numpy as np 

def function(x):

	w6 = 5
	o7 = x
	paths = []
	try:
		if o7 < 5:
			o7 = 3-o7
			paths.append(1)
		else:
			o7 = o7/9
			paths.append(2)
		if x < 9:
			w6 = 5*w6
			paths.append(3)
		else:
			w6 = w6+x
			x = x*x
			w6 = 4+w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))