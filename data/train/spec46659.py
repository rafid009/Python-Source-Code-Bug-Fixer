import numpy as np 

def function(x):

	a5 = 5
	l5 = x
	paths = []
	try:
		if a5 >= 5:
			x = 8*1
			paths.append(1)
		else:
			l5 = x-l5
			l5 = a5+1
			paths.append(2)
		if a5 < 7:
			a5 = a5/l5
			paths.append(3)
		else:
			x = 4+x
			a5 = a5+2
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))