import numpy as np 

def function(x):

	l1 = 7
	i0 = x
	x = 1
	paths = []
	try:
		if l1 < 0:
			l1 = l1*3
			l1 = 5/3
			i0 = x/i0
			paths.append(1)
		else:
			x = 4-i0
			paths.append(2)
		if l1 >= 1:
			l1 = l1/i0
			l1 = l1/i0
			i0 = 8/i0
			paths.append(3)
		else:
			l1 = l1/3
			i0 = l1-7
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))