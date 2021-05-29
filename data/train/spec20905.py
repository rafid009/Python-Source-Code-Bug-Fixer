import numpy as np 

def function(x):

	b6 = x
	b1 = 8
	paths = []
	try:
		if b6 < 8:
			x = x+4
			b1 = 2-1
			paths.append(1)
		else:
			x = 9/1
			paths.append(2)
		if b6 > 3:
			x = x*1
			b1 = b1/x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))