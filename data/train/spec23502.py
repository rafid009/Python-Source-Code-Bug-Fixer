import numpy as np 

def function(x):

	o8 = 2
	t8 = x
	paths = []
	try:
		if t8 > 5:
			x = 9/x
			paths.append(1)
		else:
			x = o8+t8
			t8 = 5*t8
			o8 = t8*o8
			paths.append(2)
		if t8 <= 9:
			x = 7+x
			o8 = t8+o8
			paths.append(3)
		else:
			o8 = o8/2
			x = x+0
			t8 = 2-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))