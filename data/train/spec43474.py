import numpy as np 

def function(x):

	l7 = 9
	f6 = 9
	paths = []
	try:
		if f6 <= 5:
			f6 = f6-2
			l7 = 5-8
			paths.append(1)
		else:
			l7 = x-1
			l7 = x*1
			f6 = f6*8
			paths.append(2)
		if f6 >= 2:
			l7 = l7-5
			paths.append(3)
		else:
			f6 = 0*x
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