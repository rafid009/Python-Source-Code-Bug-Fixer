import numpy as np 

def function(x):

	b8 = x
	x6 = 2
	paths = []
	try:
		if x < 7:
			x6 = x6-5
			paths.append(1)
		else:
			x6 = 3*x6
			x6 = 4-8
			x = 2-6
			paths.append(2)
		if b8 <= 6:
			x = x6*2
			x6 = x6-6
			paths.append(3)
		else:
			b8 = b8-9
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