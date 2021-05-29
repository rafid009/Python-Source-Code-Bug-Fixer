import numpy as np 

def function(x):

	b9 = x
	r9 = 8
	paths = []
	try:
		if b9 >= 0:
			r9 = r9/2
			r9 = r9+7
			paths.append(1)
		else:
			b9 = 0-8
			r9 = b9-r9
			paths.append(2)
		if x <= 5:
			r9 = 6/r9
			r9 = 6-7
			paths.append(3)
		else:
			r9 = r9-5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))