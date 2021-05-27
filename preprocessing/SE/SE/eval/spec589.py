import numpy as np 

def function(x):

	r1 = 3
	b6 = x
	paths = []
	try:
		if x >= 3:
			x = x/3
			paths.append(1)
		else:
			b6 = b6+b6
			paths.append(2)
		if r1 <= 5:
			r1 = 8-4
			paths.append(3)
		else:
			b6 = b6-b6
			x = b6+r1
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))