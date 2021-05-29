import numpy as np 

def function(x):

	b0 = 8
	l1 = x
	paths = []
	try:
		if l1 > 5:
			l1 = 0-6
			l1 = 1-0
			l1 = b0/l1
			paths.append(1)
		else:
			l1 = l1/b0
			b0 = 6+x
			paths.append(2)
		if l1 > 9:
			x = x+9
			paths.append(3)
		else:
			b0 = 3+b0
			x = 3+0
			l1 = l1-b0
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))