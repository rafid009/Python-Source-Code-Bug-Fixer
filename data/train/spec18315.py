import numpy as np 

def function(x):

	d2 = 6
	b0 = 8
	paths = []
	try:
		if x < 3:
			x = x-b0
			b0 = b0+1
			paths.append(1)
		else:
			b0 = 4-b0
			paths.append(2)
		if b0 >= 3:
			b0 = d2*8
			d2 = d2-x
			x = x/d2
			paths.append(3)
		else:
			x = 4/x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))