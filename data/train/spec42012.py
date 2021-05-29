import numpy as np 

def function(x):

	w8 = x
	o2 = 0
	paths = []
	try:
		if o2 >= 4:
			w8 = 4+x
			w8 = x+0
			o2 = o2/5
			paths.append(1)
		else:
			x = 6/x
			w8 = w8+1
			paths.append(2)
		if x > 8:
			o2 = 6*o2
			paths.append(3)
		else:
			o2 = o2-3
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		w8 = o2**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))