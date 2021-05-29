import numpy as np 

def function(x):

	i5 = x
	l1 = 8
	paths = []
	try:
		if x < 1:
			i5 = l1/5
			paths.append(1)
		else:
			l1 = l1*i5
			x = 2+i5
			paths.append(2)
		if x < 2:
			l1 = 4*x
			paths.append(3)
		else:
			i5 = 1/i5
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		i5 = l1**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))