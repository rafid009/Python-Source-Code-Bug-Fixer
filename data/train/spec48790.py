import numpy as np 

def function(x):

	b2 = 5
	o3 = x
	paths = []
	try:
		if b2 < 7:
			x = 5-7
			x = 9/2
			b2 = 5+b2
			paths.append(1)
		else:
			o3 = 1/7
			paths.append(2)
		if b2 <= 7:
			x = 0/x
			b2 = 9-b2
			paths.append(3)
		else:
			x = x*b2
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