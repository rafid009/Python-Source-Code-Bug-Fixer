import numpy as np 

def function(x):

	k6 = 9
	o8 = 1
	paths = []
	try:
		if o8 <= 8:
			k6 = x/9
			x = x*2
			paths.append(1)
		else:
			o8 = 5/1
			o8 = o8-4
			o8 = o8/3
			paths.append(2)
		if k6 <= 8:
			o8 = k6+o8
			x = x-6
			paths.append(3)
		else:
			k6 = k6*1
			x = x*6
			o8 = o8-8
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