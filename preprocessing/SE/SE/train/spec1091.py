import numpy as np 

def function(x):

	o8 = x
	t2 = x
	paths = []
	try:
		if o8 <= 6:
			o8 = 3*t2
			paths.append(1)
		else:
			x = x/8
			o8 = 6*4
			paths.append(2)
		if o8 > 0:
			o8 = o8/4
			paths.append(3)
		else:
			t2 = 5-t2
			x = o8-7
			t2 = o8*6
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		o8 = t2**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))