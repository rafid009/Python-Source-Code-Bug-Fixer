import numpy as np 

def function(x):

	l2 = x
	b9 = 6
	paths = []
	try:
		if l2 < 9:
			b9 = b9-1
			b9 = 9+x
			paths.append(1)
		else:
			b9 = l2+3
			x = x-8
			paths.append(2)
		if b9 < 5:
			b9 = b9/3
			x = l2-b9
			paths.append(3)
		else:
			l2 = l2-4
			x = b9/3
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		b9 = l2**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))