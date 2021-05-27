import numpy as np 

def function(x):

	i2 = 2
	l1 = x
	paths = []
	try:
		if x > 3:
			i2 = x-i2
			l1 = 5+l1
			paths.append(1)
		else:
			l1 = 0/3
			i2 = 7/7
			x = 9/x
			paths.append(2)
		if l1 > 5:
			l1 = l1/3
			x = 2+x
			paths.append(3)
		else:
			l1 = l1-3
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		i2 = l1**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))