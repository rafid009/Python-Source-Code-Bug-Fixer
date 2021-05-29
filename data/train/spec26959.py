import numpy as np 

def function(x):

	l8 = x
	i1 = 7
	paths = []
	try:
		if i1 > 7:
			x = x-8
			paths.append(1)
		else:
			i1 = i1/x
			paths.append(2)
		if i1 >= 9:
			x = x/i1
			l8 = 4+1
			paths.append(3)
		else:
			i1 = i1/6
			x = x+5
			l8 = x*l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		i1 = l8**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))