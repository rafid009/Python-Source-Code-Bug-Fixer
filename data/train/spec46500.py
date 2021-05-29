import numpy as np 

def function(x):

	y6 = 5
	b2 = x
	paths = []
	try:
		if b2 <= 1:
			y6 = y6+6
			b2 = 1+b2
			paths.append(1)
		else:
			y6 = y6+y6
			b2 = b2*9
			y6 = x+2
			paths.append(2)
		if b2 <= 5:
			b2 = b2-7
			x = x+x
			paths.append(3)
		else:
			b2 = b2+8
			y6 = y6+0
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		y6 = b2**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))