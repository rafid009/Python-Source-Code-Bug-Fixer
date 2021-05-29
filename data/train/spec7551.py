import numpy as np 

def function(x):

	o3 = x
	b8 = 9
	paths = []
	try:
		if b8 <= 6:
			o3 = o3/2
			x = x/o3
			b8 = 4+5
			paths.append(1)
		else:
			b8 = 3*b8
			paths.append(2)
		if o3 >= 0:
			b8 = o3*6
			b8 = b8*x
			x = 2-0
			paths.append(3)
		else:
			b8 = 6-o3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		b8 = o3**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))