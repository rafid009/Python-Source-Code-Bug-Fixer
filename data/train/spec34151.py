import numpy as np 

def function(x):

	b1 = 8
	b3 = 4
	paths = []
	try:
		if b3 <= 9:
			b3 = 9/1
			paths.append(1)
		else:
			b1 = x/1
			paths.append(2)
		if b1 >= 4:
			b3 = x/x
			x = x*4
			b3 = x/b1
			paths.append(3)
		else:
			b1 = 7/6
			x = x/x
			b3 = 0/b3
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