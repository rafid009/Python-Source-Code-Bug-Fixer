import numpy as np 

def function(x):

	l3 = x
	y7 = 1
	paths = []
	try:
		if y7 < 1:
			x = x*2
			paths.append(1)
		else:
			l3 = l3/2
			y7 = x-y7
			paths.append(2)
		if x <= 6:
			x = y7-x
			l3 = 6*2
			x = x*l3
			paths.append(3)
		else:
			x = x+y7
			y7 = 3+1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		l3 = y7**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))