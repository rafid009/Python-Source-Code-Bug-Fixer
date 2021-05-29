import numpy as np 

def function(x):

	b9 = 5
	b3 = 1
	paths = []
	try:
		if b9 <= 5:
			b9 = b3-b9
			b3 = b3*1
			paths.append(1)
		else:
			x = x/b3
			paths.append(2)
		if b9 <= 2:
			b3 = b3/b3
			b3 = 6*b3
			paths.append(3)
		else:
			b3 = 1-x
			b3 = b3-b9
			b3 = 6*b3
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b3 = b9**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))