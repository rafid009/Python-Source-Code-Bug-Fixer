import numpy as np 

def function(x):

	o2 = x
	f6 = 3
	x = 8
	paths = []
	try:
		if o2 >= 6:
			x = x-1
			paths.append(1)
		else:
			f6 = 3-f6
			paths.append(2)
		if o2 >= 7:
			f6 = f6+3
			x = f6-x
			f6 = f6-o2
			paths.append(3)
		else:
			x = 3+7
			o2 = o2/x
			o2 = o2*2
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