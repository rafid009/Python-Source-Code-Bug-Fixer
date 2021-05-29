import numpy as np 

def function(x):

	w6 = x
	o2 = 1
	paths = []
	try:
		if w6 > 4:
			x = x+1
			w6 = w6-w6
			w6 = o2-9
			paths.append(1)
		else:
			w6 = 4+w6
			paths.append(2)
		if o2 < 9:
			x = 7+x
			paths.append(3)
		else:
			x = o2-x
			o2 = 3+o2
			w6 = w6-9
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