import numpy as np 

def function(x):

	l6 = 3
	r7 = 3
	paths = []
	try:
		if l6 <= 3:
			r7 = 6/5
			l6 = x*8
			paths.append(1)
		else:
			x = 6*7
			x = 2*8
			x = l6+x
			paths.append(2)
		if x >= 5:
			l6 = 3+r7
			r7 = 4/8
			paths.append(3)
		else:
			l6 = l6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))