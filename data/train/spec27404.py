import numpy as np 

def function(x):

	b7 = x
	o1 = 8
	paths = []
	try:
		if o1 > 2:
			x = x/5
			paths.append(1)
		else:
			b7 = 5/b7
			x = 7+x
			paths.append(2)
		if o1 < 5:
			x = 4-x
			x = x/3
			b7 = o1*9
			paths.append(3)
		else:
			b7 = 9-b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))