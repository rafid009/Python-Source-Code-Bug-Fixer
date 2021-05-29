import numpy as np 

def function(x):

	e5 = 8
	o3 = x
	paths = []
	try:
		if x > 4:
			x = 8+e5
			o3 = 9*8
			o3 = x/8
			paths.append(1)
		else:
			o3 = e5*o3
			paths.append(2)
		if x > 6:
			x = x-e5
			x = e5*o3
			x = 1-1
			paths.append(3)
		else:
			e5 = x*x
			x = 0+x
			o3 = o3+3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		x = o3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))