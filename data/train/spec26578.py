import numpy as np 

def function(x):

	l3 = 0
	paths = []
	try:
		if x < 3:
			l3 = l3-7
			paths.append(1)
		else:
			x = 2*x
			l3 = 7-l3
			paths.append(2)
		if l3 < 9:
			x = 4+x
			x = 0*x
			x = x-0
			paths.append(3)
		else:
			l3 = l3+x
			l3 = x-8
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