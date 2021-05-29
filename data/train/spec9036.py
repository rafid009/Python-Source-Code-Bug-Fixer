import numpy as np 

def function(x):

	o2 = 6
	w8 = x
	paths = []
	try:
		if o2 > 6:
			o2 = 4+x
			paths.append(1)
		else:
			x = x/w8
			x = 4*7
			paths.append(2)
		if w8 < 7:
			o2 = o2+x
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))