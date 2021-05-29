import numpy as np 

def function(x):

	b8 = x
	l8 = x
	x = 4
	paths = []
	try:
		if b8 <= 5:
			l8 = l8+7
			l8 = x/3
			paths.append(1)
		else:
			b8 = b8*4
			paths.append(2)
		if x > 9:
			b8 = 8+0
			l8 = x+l8
			paths.append(3)
		else:
			l8 = b8-l8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		l8 = b8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))