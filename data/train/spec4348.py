import numpy as np 

def function(x):

	f1 = 3
	o3 = 2
	paths = []
	try:
		if o3 > 6:
			o3 = o3+1
			paths.append(1)
		else:
			o3 = o3/8
			paths.append(2)
		if f1 <= 6:
			o3 = o3+1
			paths.append(3)
		else:
			x = 2-x
			o3 = o3+f1
			f1 = f1/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))