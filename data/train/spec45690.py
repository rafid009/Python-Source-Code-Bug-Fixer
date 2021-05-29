import numpy as np 

def function(x):

	l1 = x
	b6 = x
	x = 1
	paths = []
	try:
		if l1 < 6:
			b6 = 8/b6
			l1 = 4/b6
			x = x-1
			paths.append(1)
		else:
			x = b6/8
			paths.append(2)
		if l1 > 2:
			x = x*7
			b6 = b6/1
			paths.append(3)
		else:
			x = 8-1
			x = l1-9
			b6 = b6*2
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		b6 = l1**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))