import numpy as np 

def function(x):

	l1 = 3
	i7 = x
	paths = []
	try:
		if i7 <= 6:
			x = i7-i7
			paths.append(1)
		else:
			l1 = 4/l1
			i7 = 8/5
			paths.append(2)
		if x >= 0:
			i7 = i7*2
			x = i7+5
			x = x+l1
			paths.append(3)
		else:
			l1 = l1+i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))