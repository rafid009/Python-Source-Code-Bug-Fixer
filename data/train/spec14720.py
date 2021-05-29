import numpy as np 

def function(x):

	l9 = x
	b9 = x
	paths = []
	try:
		if x > 4:
			b9 = b9-9
			paths.append(1)
		else:
			b9 = b9/4
			b9 = b9+1
			paths.append(2)
		if l9 >= 2:
			l9 = l9+6
			b9 = 6*b9
			l9 = 0+l9
			paths.append(3)
		else:
			b9 = 3/8
			l9 = l9*l9
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