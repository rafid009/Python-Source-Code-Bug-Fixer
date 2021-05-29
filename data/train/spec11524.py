import numpy as np 

def function(x):

	o8 = x
	t4 = x
	paths = []
	try:
		if t4 <= 6:
			t4 = t4+t4
			paths.append(1)
		else:
			o8 = x-t4
			x = x*1
			x = 2*1
			paths.append(2)
		if o8 < 4:
			o8 = o8-t4
			o8 = x/o8
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))