import numpy as np 

def function(x):

	o3 = 2
	l2 = x
	x = x
	paths = []
	try:
		if l2 < 0:
			o3 = 0+l2
			paths.append(1)
		else:
			x = x-5
			x = 5-x
			l2 = 3/o3
			paths.append(2)
		if x < 1:
			l2 = l2*x
			l2 = l2+4
			paths.append(3)
		else:
			o3 = 3*o3
			o3 = o3*3
			x = x*l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		o3 = l2**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))