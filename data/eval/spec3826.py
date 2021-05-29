import numpy as np 

def function(x):

	h8 = x
	l7 = 9
	x = x
	paths = []
	try:
		if l7 >= 6:
			l7 = 1*x
			paths.append(1)
		else:
			x = h8+h8
			h8 = x-6
			paths.append(2)
		if x >= 7:
			l7 = 4/l7
			x = l7+x
			l7 = l7+7
			paths.append(3)
		else:
			x = x+x
			x = x/3
			h8 = h8*1
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))