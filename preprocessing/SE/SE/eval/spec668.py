import numpy as np 

def function(x):

	w8 = x
	o2 = x
	paths = []
	try:
		if o2 >= 7:
			w8 = 6/w8
			w8 = w8-7
			paths.append(1)
		else:
			w8 = x+w8
			paths.append(2)
		if x <= 5:
			w8 = o2/o2
			o2 = x*1
			o2 = 9-9
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))