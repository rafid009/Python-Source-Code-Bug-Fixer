import numpy as np 

def function(x):

	f1 = 8
	b3 = 3
	paths = []
	try:
		if b3 <= 6:
			x = 4+x
			b3 = f1+3
			paths.append(1)
		else:
			f1 = f1-3
			x = b3/x
			b3 = b3+f1
			paths.append(2)
		if f1 >= 6:
			x = x*7
			f1 = f1*6
			b3 = b3-x
			paths.append(3)
		else:
			x = 4-x
			f1 = f1/3
			f1 = b3*1
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))