import numpy as np 

def function(x):

	t6 = 8
	o1 = x
	paths = []
	try:
		if t6 > 2:
			x = 0-8
			o1 = x+6
			t6 = x-6
			paths.append(1)
		else:
			o1 = o1*o1
			x = 0*t6
			paths.append(2)
		if o1 >= 7:
			t6 = 3*t6
			t6 = t6/6
			paths.append(3)
		else:
			o1 = o1*o1
			o1 = o1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))