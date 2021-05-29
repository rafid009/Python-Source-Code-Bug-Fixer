import numpy as np 

def function(x):

	l2 = x
	i5 = 1
	paths = []
	try:
		if x >= 0:
			i5 = i5+0
			i5 = i5-0
			paths.append(1)
		else:
			i5 = i5+l2
			paths.append(2)
		if x <= 4:
			i5 = 0+i5
			x = x-4
			l2 = l2-8
			paths.append(3)
		else:
			i5 = i5-0
			i5 = 8+i5
			l2 = l2/i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))