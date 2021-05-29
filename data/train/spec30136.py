import numpy as np 

def function(x):

	p7 = 5
	b3 = x
	paths = []
	try:
		if x <= 3:
			b3 = p7*x
			p7 = 9-p7
			x = x-4
			paths.append(1)
		else:
			b3 = 3/1
			paths.append(2)
		if x < 9:
			b3 = x-3
			p7 = p7-6
			x = x/2
			paths.append(3)
		else:
			b3 = b3*9
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))