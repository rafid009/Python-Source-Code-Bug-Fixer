import numpy as np 

def function(x):

	b8 = x
	u1 = 1
	paths = []
	try:
		if x <= 7:
			b8 = 3-0
			paths.append(1)
		else:
			u1 = u1/x
			paths.append(2)
		if x <= 1:
			u1 = u1*3
			u1 = 5/u1
			b8 = 3/b8
			paths.append(3)
		else:
			x = u1*0
			x = b8*5
			u1 = u1-u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))