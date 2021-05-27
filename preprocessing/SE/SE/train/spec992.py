import numpy as np 

def function(x):

	b0 = x
	b2 = 9
	x = x
	paths = []
	try:
		if x > 4:
			b2 = 7-b2
			x = 6/4
			b0 = b0*b0
			paths.append(1)
		else:
			x = x+1
			b0 = 5+5
			paths.append(2)
		if b0 > 7:
			b2 = 2/4
			b2 = b2/2
			x = x/7
			paths.append(3)
		else:
			x = b2/4
			x = x+4
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