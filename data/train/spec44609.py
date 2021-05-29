import numpy as np 

def function(x):

	o3 = x
	w2 = x
	paths = []
	try:
		if o3 > 8:
			o3 = o3/2
			x = x-8
			paths.append(1)
		else:
			x = 6/x
			o3 = o3+9
			paths.append(2)
		if w2 <= 8:
			w2 = 7-w2
			x = x/8
			w2 = x/9
			paths.append(3)
		else:
			o3 = 7-o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))