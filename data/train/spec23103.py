import numpy as np 

def function(x):

	f3 = x
	l7 = x
	paths = []
	try:
		if l7 > 8:
			x = x+2
			l7 = l7/x
			paths.append(1)
		else:
			x = 1+7
			f3 = f3+3
			x = x+9
			paths.append(2)
		if f3 > 2:
			l7 = 0-7
			paths.append(3)
		else:
			x = f3+8
			f3 = 4*x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		f3 = l7**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))