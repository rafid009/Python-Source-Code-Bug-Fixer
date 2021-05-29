import numpy as np 

def function(x):

	o8 = 5
	o2 = x
	paths = []
	try:
		if o8 <= 9:
			x = x-6
			o2 = o2*1
			paths.append(1)
		else:
			o8 = o2-o8
			o8 = 7+o8
			paths.append(2)
		if o2 <= 4:
			x = x*1
			o2 = 1+o2
			paths.append(3)
		else:
			o8 = 0/7
			o8 = o8-2
			x = x*5
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