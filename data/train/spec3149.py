import numpy as np 

def function(x):

	l2 = x
	i1 = 4
	paths = []
	try:
		if i1 > 1:
			l2 = x/3
			i1 = x-0
			x = x/9
			paths.append(1)
		else:
			i1 = 6-i1
			x = x/8
			paths.append(2)
		if x > 1:
			i1 = i1/8
			paths.append(3)
		else:
			i1 = 6/i1
			l2 = l2-7
			l2 = 1*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))