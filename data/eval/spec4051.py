import numpy as np 

def function(x):

	l7 = 6
	b3 = x
	paths = []
	try:
		if l7 >= 0:
			l7 = 2-9
			x = x*b3
			b3 = b3+5
			paths.append(1)
		else:
			x = 7*b3
			paths.append(2)
		if b3 >= 3:
			l7 = 4/l7
			b3 = 7/9
			b3 = b3+8
			paths.append(3)
		else:
			b3 = b3/8
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		l7 = b3**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))