import numpy as np 

def function(x):

	t1 = x
	o8 = 3
	paths = []
	try:
		if t1 >= 6:
			t1 = x*o8
			paths.append(1)
		else:
			o8 = t1-x
			o8 = o8+t1
			paths.append(2)
		if x < 4:
			t1 = t1/x
			paths.append(3)
		else:
			o8 = 6/1
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