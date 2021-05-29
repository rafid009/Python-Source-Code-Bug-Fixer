import numpy as np 

def function(x):

	l3 = x
	x2 = x
	paths = []
	try:
		if x > 5:
			x2 = 4-7
			paths.append(1)
		else:
			x2 = 2-6
			paths.append(2)
		if x2 >= 6:
			l3 = l3*8
			l3 = l3*4
			x = 3+x
			paths.append(3)
		else:
			x2 = 4-l3
			x2 = l3-4
			x2 = x/x2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x2 = l3**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))