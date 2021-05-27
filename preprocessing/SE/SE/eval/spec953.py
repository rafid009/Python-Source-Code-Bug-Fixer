import numpy as np 

def function(x):

	q0 = x
	o3 = x
	paths = []
	try:
		if q0 > 4:
			o3 = x/7
			paths.append(1)
		else:
			q0 = o3+1
			paths.append(2)
		if o3 >= 2:
			q0 = 6-q0
			o3 = q0-x
			x = x-1
			paths.append(3)
		else:
			x = x-3
			x = q0-2
			o3 = o3*4
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		o3 = q0**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))