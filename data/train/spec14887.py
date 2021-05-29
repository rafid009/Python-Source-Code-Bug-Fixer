import numpy as np 

def function(x):

	l6 = x
	i6 = 1
	paths = []
	try:
		if l6 <= 9:
			i6 = i6*7
			x = x/x
			x = i6-x
			paths.append(1)
		else:
			x = x+1
			x = l6/x
			l6 = 3-0
			paths.append(2)
		if x >= 9:
			x = 1+4
			paths.append(3)
		else:
			i6 = l6-4
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		i6 = l6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))