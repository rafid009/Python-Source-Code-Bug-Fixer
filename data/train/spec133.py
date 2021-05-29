import numpy as np 

def function(x):

	l8 = x
	b6 = 4
	paths = []
	try:
		if b6 > 7:
			l8 = l8+x
			l8 = 4-l8
			paths.append(1)
		else:
			x = x+1
			b6 = b6/2
			paths.append(2)
		if b6 >= 0:
			x = 6+6
			paths.append(3)
		else:
			x = x-7
			b6 = b6/1
			b6 = 9/b6
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		b6 = l8**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))