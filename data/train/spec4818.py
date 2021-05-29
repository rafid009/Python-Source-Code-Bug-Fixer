import numpy as np 

def function(x):

	x9 = x
	b3 = 1
	paths = []
	try:
		if x <= 6:
			b3 = 5*x9
			paths.append(1)
		else:
			x = x9-4
			paths.append(2)
		if x < 1:
			x9 = x/6
			x = x+5
			paths.append(3)
		else:
			b3 = 5-b3
			x = x-3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))