import numpy as np 

def function(x):

	d1 = x
	b3 = 9
	paths = []
	try:
		if b3 >= 7:
			d1 = 8*d1
			paths.append(1)
		else:
			b3 = b3/b3
			b3 = 0*4
			x = x+1
			paths.append(2)
		if x >= 5:
			d1 = 8-b3
			x = 7*2
			paths.append(3)
		else:
			b3 = x-b3
			b3 = 8*4
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))