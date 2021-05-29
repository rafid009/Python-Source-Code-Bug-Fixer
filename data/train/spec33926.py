import numpy as np 

def function(x):

	l6 = 0
	i9 = x
	paths = []
	try:
		if i9 < 4:
			i9 = 3/x
			i9 = l6/8
			x = i9-8
			paths.append(1)
		else:
			x = x/2
			i9 = 7*3
			l6 = 1+l6
			paths.append(2)
		if i9 >= 5:
			x = l6+3
			x = l6/8
			paths.append(3)
		else:
			i9 = 6+0
			l6 = 2+i9
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))