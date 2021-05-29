import numpy as np 

def function(x):

	b1 = x
	l1 = x
	x = x
	paths = []
	try:
		if b1 <= 1:
			l1 = l1/3
			b1 = l1+l1
			paths.append(1)
		else:
			x = x+x
			b1 = 8+b1
			paths.append(2)
		if b1 > 2:
			b1 = 0+b1
			paths.append(3)
		else:
			b1 = 7+b1
			x = x+1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		b1 = l1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))