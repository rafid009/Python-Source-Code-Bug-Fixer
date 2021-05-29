import numpy as np 

def function(x):

	p9 = 7
	l6 = 5
	paths = []
	try:
		if l6 <= 4:
			l6 = p9*8
			paths.append(1)
		else:
			x = x-9
			p9 = 3+p9
			paths.append(2)
		if l6 >= 0:
			x = 8-x
			p9 = 6+p9
			paths.append(3)
		else:
			x = x*p9
			p9 = p9/6
			l6 = 1/l6
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