import numpy as np 

def function(x):

	e9 = x
	b2 = 6
	paths = []
	try:
		if x > 6:
			b2 = b2+b2
			paths.append(1)
		else:
			x = b2/8
			paths.append(2)
		if x <= 8:
			x = x*8
			b2 = b2-9
			paths.append(3)
		else:
			b2 = 1*b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))