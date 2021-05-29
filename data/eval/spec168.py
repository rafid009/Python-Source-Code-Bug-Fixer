import numpy as np 

def function(x):

	i6 = x
	l2 = 2
	paths = []
	try:
		if l2 <= 5:
			l2 = 4+l2
			paths.append(1)
		else:
			i6 = i6-4
			x = x/l2
			x = 2-2
			paths.append(2)
		if x >= 4:
			l2 = 5-l2
			paths.append(3)
		else:
			l2 = l2*3
			x = x+l2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))