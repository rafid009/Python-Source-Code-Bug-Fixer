import numpy as np 

def function(x):

	b2 = x
	f7 = x
	paths = []
	try:
		if x < 0:
			f7 = f7-b2
			b2 = 0/x
			paths.append(1)
		else:
			x = 7+4
			x = x+x
			b2 = b2-2
			paths.append(2)
		if b2 <= 3:
			f7 = f7+4
			b2 = b2+8
			b2 = b2+4
			paths.append(3)
		else:
			f7 = f7*x
			b2 = b2*6
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