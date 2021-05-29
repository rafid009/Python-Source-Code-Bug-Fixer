import numpy as np 

def function(x):

	b2 = 9
	v8 = x
	paths = []
	try:
		if v8 >= 3:
			v8 = v8*2
			v8 = 9-x
			b2 = v8*b2
			paths.append(1)
		else:
			v8 = v8-6
			b2 = b2-3
			paths.append(2)
		if b2 <= 9:
			x = 6-5
			b2 = 3*v8
			paths.append(3)
		else:
			v8 = v8/b2
			b2 = b2/6
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))