import numpy as np 

def function(x):

	l7 = x
	b1 = x
	paths = []
	try:
		if x > 1:
			b1 = b1/b1
			l7 = l7/l7
			paths.append(1)
		else:
			l7 = 9-1
			paths.append(2)
		if l7 <= 0:
			b1 = 8+b1
			l7 = l7*8
			paths.append(3)
		else:
			l7 = l7/l7
			l7 = l7+b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))