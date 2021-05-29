import numpy as np 

def function(x):

	b8 = 3
	q5 = x
	paths = []
	try:
		if b8 >= 3:
			q5 = b8*3
			paths.append(1)
		else:
			x = 8/x
			q5 = 3-5
			b8 = 8-2
			paths.append(2)
		if x > 1:
			b8 = b8+q5
			q5 = 1/q5
			paths.append(3)
		else:
			b8 = 3-x
			b8 = b8-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))