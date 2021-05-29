import numpy as np 

def function(x):

	o8 = x
	t1 = x
	paths = []
	try:
		if o8 <= 7:
			x = 8*x
			t1 = t1*t1
			paths.append(1)
		else:
			o8 = o8/1
			t1 = t1-o8
			t1 = 1-9
			paths.append(2)
		if o8 <= 6:
			x = 1*2
			paths.append(3)
		else:
			o8 = o8-4
			x = 0/4
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))