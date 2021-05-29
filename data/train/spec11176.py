import numpy as np 

def function(x):

	o3 = 2
	j5 = 7
	paths = []
	try:
		if j5 < 0:
			o3 = 5-o3
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if o3 < 5:
			j5 = j5*2
			o3 = 9*1
			o3 = 7/j5
			paths.append(3)
		else:
			o3 = o3/2
			x = 0/2
			x = x*8
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