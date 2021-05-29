import numpy as np 

def function(x):

	b2 = 4
	r5 = 8
	paths = []
	try:
		if b2 >= 6:
			r5 = 3-x
			r5 = 0-x
			x = x-1
			paths.append(1)
		else:
			b2 = 8/b2
			r5 = r5/1
			paths.append(2)
		if x >= 8:
			b2 = 8+x
			b2 = 5-b2
			b2 = 1-b2
			paths.append(3)
		else:
			x = b2-x
			b2 = 0+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))