import numpy as np 

def function(x):

	y4 = x
	l9 = x
	paths = []
	try:
		if y4 <= 2:
			x = x+x
			paths.append(1)
		else:
			x = x+y4
			l9 = x-3
			paths.append(2)
		if l9 <= 1:
			l9 = y4/4
			paths.append(3)
		else:
			y4 = 0/1
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))