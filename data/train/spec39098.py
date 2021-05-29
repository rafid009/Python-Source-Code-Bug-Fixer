import numpy as np 

def function(x):

	l1 = 0
	l2 = x
	x = x
	paths = []
	try:
		if l1 < 8:
			x = x-6
			paths.append(1)
		else:
			l1 = l1+5
			l1 = 9*8
			paths.append(2)
		if l2 <= 4:
			l2 = l2/l2
			x = l2-7
			l1 = l1+x
			paths.append(3)
		else:
			l1 = l1+9
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