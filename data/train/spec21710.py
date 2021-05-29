import numpy as np 

def function(x):

	w6 = x
	o4 = 1
	paths = []
	try:
		if x <= 0:
			o4 = o4*2
			paths.append(1)
		else:
			x = x+1
			o4 = 0-o4
			o4 = o4+o4
			paths.append(2)
		if o4 < 7:
			o4 = o4+0
			paths.append(3)
		else:
			x = o4+o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		w6 = o4**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))