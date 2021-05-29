import numpy as np 

def function(x):

	b7 = 7
	b6 = 4
	paths = []
	try:
		if b7 < 6:
			b7 = 7+b7
			x = 2*x
			paths.append(1)
		else:
			b6 = b7-5
			b6 = 0-7
			b6 = b6/9
			paths.append(2)
		if x <= 7:
			b7 = b7+0
			b7 = b7*9
			x = x-7
			paths.append(3)
		else:
			b7 = 6+b7
			b7 = 4-x
			b7 = 2-b6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b7 = b6**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))