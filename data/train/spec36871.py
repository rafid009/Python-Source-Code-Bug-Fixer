import numpy as np 

def function(x):

	b0 = x
	x6 = 8
	paths = []
	try:
		if b0 < 3:
			x6 = b0+x6
			x6 = x+4
			paths.append(1)
		else:
			b0 = 4/b0
			paths.append(2)
		if b0 <= 5:
			x = 8-x6
			x6 = x6+5
			x6 = x*8
			paths.append(3)
		else:
			x6 = x*x6
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x6 = b0**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))