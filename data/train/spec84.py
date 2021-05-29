import numpy as np 

def function(x):

	f3 = 1
	o8 = x
	paths = []
	try:
		if o8 > 5:
			f3 = 5/8
			paths.append(1)
		else:
			f3 = f3-0
			x = f3+7
			x = 5*f3
			paths.append(2)
		if x >= 2:
			o8 = o8*4
			paths.append(3)
		else:
			f3 = 9/5
			f3 = f3+7
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		f3 = o8**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))