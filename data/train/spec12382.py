import numpy as np 

def function(x):

	n8 = x
	l4 = 0
	paths = []
	try:
		if x < 7:
			n8 = 4-x
			paths.append(1)
		else:
			x = x+x
			n8 = n8*7
			paths.append(2)
		if x <= 1:
			x = x*9
			n8 = n8+4
			paths.append(3)
		else:
			l4 = x/x
			x = x+x
			l4 = x/l4
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		l4 = n8**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))