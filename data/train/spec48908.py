import numpy as np 

def function(x):

	o2 = x
	w6 = 9
	paths = []
	try:
		if w6 <= 8:
			o2 = 5*o2
			w6 = 5/1
			x = x/4
			paths.append(1)
		else:
			o2 = w6+o2
			w6 = w6-3
			w6 = 6+w6
			paths.append(2)
		if o2 <= 4:
			o2 = 2-6
			o2 = o2*3
			paths.append(3)
		else:
			w6 = x-7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))