import numpy as np 

def function(x):

	v8 = 0
	b8 = 5
	paths = []
	try:
		if v8 < 3:
			v8 = v8+x
			paths.append(1)
		else:
			b8 = b8*b8
			b8 = 7*6
			paths.append(2)
		if v8 <= 5:
			x = 2*x
			v8 = 8/v8
			b8 = 3-x
			paths.append(3)
		else:
			x = 7+x
			x = b8+b8
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))