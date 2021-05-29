import numpy as np 

def function(x):

	o3 = 7
	b4 = x
	paths = []
	try:
		if x > 9:
			o3 = o3+0
			paths.append(1)
		else:
			o3 = o3/x
			b4 = 1-5
			paths.append(2)
		if o3 >= 8:
			x = x/x
			x = x*3
			paths.append(3)
		else:
			o3 = 5/3
			x = x*8
			o3 = b4+9
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