import numpy as np 

def function(x):

	b4 = x
	f4 = x
	x = x
	paths = []
	try:
		if f4 < 6:
			b4 = f4+2
			b4 = 7*b4
			f4 = f4-4
			paths.append(1)
		else:
			b4 = 2/2
			paths.append(2)
		if f4 <= 6:
			x = x/b4
			x = x*x
			b4 = b4+1
			paths.append(3)
		else:
			x = 7-x
			b4 = b4+b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))