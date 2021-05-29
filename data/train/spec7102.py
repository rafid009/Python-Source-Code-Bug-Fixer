import numpy as np 

def function(x):

	l4 = x
	q4 = x
	x = 9
	paths = []
	try:
		if l4 >= 3:
			q4 = 8+q4
			q4 = q4+7
			paths.append(1)
		else:
			l4 = x/x
			paths.append(2)
		if l4 <= 9:
			l4 = 8*l4
			l4 = l4*9
			l4 = x+9
			paths.append(3)
		else:
			l4 = 2-6
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))