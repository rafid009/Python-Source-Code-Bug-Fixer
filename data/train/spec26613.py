import numpy as np 

def function(x):

	r7 = 9
	l4 = 1
	paths = []
	try:
		if r7 > 1:
			l4 = l4+7
			paths.append(1)
		else:
			l4 = r7*4
			x = 5*8
			paths.append(2)
		if r7 <= 8:
			r7 = r7+r7
			x = x-x
			r7 = r7*1
			paths.append(3)
		else:
			r7 = r7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))