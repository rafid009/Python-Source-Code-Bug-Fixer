import numpy as np 

def function(x):

	l1 = x
	o7 = x
	x = x
	paths = []
	try:
		if l1 > 1:
			x = l1/x
			paths.append(1)
		else:
			l1 = l1+l1
			l1 = l1-7
			o7 = o7-6
			paths.append(2)
		if l1 <= 4:
			x = 4-x
			paths.append(3)
		else:
			l1 = 2+6
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