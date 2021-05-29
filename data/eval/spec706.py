import numpy as np 

def function(x):

	w2 = x
	o2 = 8
	paths = []
	try:
		if o2 <= 6:
			x = x*5
			x = x-x
			o2 = o2*8
			paths.append(1)
		else:
			w2 = 9*6
			x = x-1
			x = x/9
			paths.append(2)
		if o2 >= 9:
			x = x/o2
			paths.append(3)
		else:
			o2 = o2/x
			w2 = o2-6
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