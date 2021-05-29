import numpy as np 

def function(x):

	l4 = 2
	x6 = 9
	x = x
	paths = []
	try:
		if l4 <= 7:
			x6 = l4+x
			x6 = x6-9
			paths.append(1)
		else:
			x = 5+5
			x = x+1
			x6 = x6+x6
			paths.append(2)
		if l4 >= 1:
			l4 = 6+l4
			l4 = x-l4
			x = x/6
			paths.append(3)
		else:
			l4 = l4-x6
			x6 = 2/x6
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x6 = l4**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))