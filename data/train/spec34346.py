import numpy as np 

def function(x):

	p7 = 8
	l7 = x
	paths = []
	try:
		if l7 >= 0:
			p7 = p7*3
			x = p7/8
			p7 = p7-l7
			paths.append(1)
		else:
			p7 = 5+p7
			x = x/9
			paths.append(2)
		if x <= 1:
			x = x+2
			p7 = 8-x
			l7 = l7+0
			paths.append(3)
		else:
			l7 = 8/l7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		l7 = p7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))