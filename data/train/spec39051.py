import numpy as np 

def function(x):

	l7 = x
	l2 = x
	paths = []
	try:
		if l7 >= 7:
			l2 = 9-7
			paths.append(1)
		else:
			l2 = l2*3
			x = l7+6
			x = 0*x
			paths.append(2)
		if x < 8:
			x = x-4
			l2 = l2+l2
			paths.append(3)
		else:
			l7 = l7/1
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))