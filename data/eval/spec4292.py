import numpy as np 

def function(x):

	v8 = x
	b8 = x
	paths = []
	try:
		if x <= 4:
			b8 = v8-6
			paths.append(1)
		else:
			v8 = 4+v8
			paths.append(2)
		if x >= 1:
			b8 = 6-b8
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))