import numpy as np 

def function(x):

	x2 = x
	b4 = x
	paths = []
	try:
		if b4 >= 7:
			b4 = 0/1
			paths.append(1)
		else:
			x2 = x-6
			paths.append(2)
		if x <= 8:
			x = x/9
			x = 1+x
			paths.append(3)
		else:
			b4 = 9*5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))