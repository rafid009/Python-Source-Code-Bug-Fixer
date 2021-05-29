import numpy as np 

def function(x):

	b5 = x
	o9 = x
	paths = []
	try:
		if b5 >= 3:
			x = o9/2
			b5 = 4*4
			paths.append(1)
		else:
			x = o9*1
			x = 3+x
			paths.append(2)
		if x < 6:
			b5 = b5*5
			o9 = 4-x
			b5 = b5+2
			paths.append(3)
		else:
			o9 = x+x
			x = o9-8
			b5 = x/b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))