import numpy as np 

def function(x):

	b3 = x
	n4 = x
	x = 5
	paths = []
	try:
		if b3 < 6:
			x = x/n4
			paths.append(1)
		else:
			n4 = 9-n4
			x = x+n4
			paths.append(2)
		if n4 > 4:
			b3 = 8*x
			x = x-8
			paths.append(3)
		else:
			x = x*1
			b3 = b3-x
			n4 = 7+n4
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