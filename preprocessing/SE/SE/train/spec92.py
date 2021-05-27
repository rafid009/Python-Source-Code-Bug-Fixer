import numpy as np 

def function(x):

	l2 = 7
	p3 = 0
	paths = []
	try:
		if x < 4:
			l2 = 6-l2
			l2 = x-6
			paths.append(1)
		else:
			p3 = p3+5
			l2 = l2+9
			p3 = p3/5
			paths.append(2)
		if x < 7:
			l2 = 7+x
			paths.append(3)
		else:
			x = p3-7
			x = 5*5
			l2 = l2*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))