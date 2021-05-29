import numpy as np 

def function(x):

	b2 = 9
	b8 = x
	paths = []
	try:
		if x < 4:
			b2 = 1*b2
			b8 = b8-3
			b2 = x+2
			paths.append(1)
		else:
			x = x/b2
			b2 = 4+b2
			b8 = 6+9
			paths.append(2)
		if x > 8:
			b2 = 8-b2
			b2 = 6-b2
			b8 = x+2
			paths.append(3)
		else:
			b8 = 4/2
			x = x*b8
			b8 = 9/8
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