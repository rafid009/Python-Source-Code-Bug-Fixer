import numpy as np 

def function(x):

	o3 = 1
	q0 = x
	paths = []
	try:
		if x < 4:
			x = x*4
			x = x-0
			o3 = q0+6
			paths.append(1)
		else:
			x = o3+x
			paths.append(2)
		if o3 < 6:
			q0 = 4+q0
			q0 = x+1
			paths.append(3)
		else:
			q0 = o3*q0
			x = o3/4
			o3 = o3-8
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		q0 = o3**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))