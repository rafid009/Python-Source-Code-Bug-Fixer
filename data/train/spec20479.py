import numpy as np 

def function(x):

	l3 = x
	f1 = 7
	paths = []
	try:
		if x < 0:
			x = 9+x
			paths.append(1)
		else:
			f1 = 8/l3
			f1 = f1*f1
			paths.append(2)
		if x < 3:
			x = x*8
			l3 = 0/4
			x = f1-1
			paths.append(3)
		else:
			x = x*3
			l3 = l3*x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))