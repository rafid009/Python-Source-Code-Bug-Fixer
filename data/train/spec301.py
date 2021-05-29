import numpy as np 

def function(x):

	b5 = 7
	u2 = x
	paths = []
	try:
		if b5 > 9:
			x = x*8
			b5 = x-b5
			paths.append(1)
		else:
			b5 = 8*b5
			paths.append(2)
		if x > 7:
			u2 = 8-u2
			b5 = b5*4
			paths.append(3)
		else:
			b5 = 6-b5
			b5 = b5*7
			u2 = u2-3
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		b5 = u2**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))