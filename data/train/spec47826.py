import numpy as np 

def function(x):

	d7 = x
	b4 = 8
	paths = []
	try:
		if x <= 3:
			d7 = d7/x
			b4 = 2-b4
			paths.append(1)
		else:
			b4 = b4/d7
			b4 = b4*4
			d7 = 7-8
			paths.append(2)
		if d7 <= 9:
			b4 = 9/d7
			paths.append(3)
		else:
			x = 7-8
			d7 = 5+x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))