import numpy as np 

def function(x):

	b9 = 4
	l5 = 7
	paths = []
	try:
		if l5 >= 9:
			b9 = 8/b9
			b9 = b9+1
			paths.append(1)
		else:
			b9 = b9-8
			l5 = l5*x
			paths.append(2)
		if b9 >= 1:
			x = l5+x
			paths.append(3)
		else:
			x = x/l5
			b9 = 6/b9
			x = l5*5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))