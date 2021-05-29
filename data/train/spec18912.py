import numpy as np 

def function(x):

	e5 = x
	b1 = 8
	paths = []
	try:
		if b1 <= 7:
			x = 0+x
			b1 = b1+x
			paths.append(1)
		else:
			b1 = x*e5
			b1 = b1/e5
			e5 = 9*8
			paths.append(2)
		if b1 < 5:
			x = x+9
			x = 8+x
			paths.append(3)
		else:
			b1 = b1/2
			x = 2*1
			b1 = b1/4
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))