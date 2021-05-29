import numpy as np 

def function(x):

	b7 = 7
	o3 = x
	x = 7
	paths = []
	try:
		if o3 >= 3:
			b7 = 5+b7
			o3 = o3*8
			paths.append(1)
		else:
			x = 7-4
			paths.append(2)
		if o3 <= 8:
			b7 = 1*x
			b7 = b7+o3
			x = 6/x
			paths.append(3)
		else:
			x = x*0
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