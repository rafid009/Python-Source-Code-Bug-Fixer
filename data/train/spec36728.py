import numpy as np 

def function(x):

	b2 = x
	l6 = 7
	paths = []
	try:
		if x > 8:
			x = x+5
			x = x-7
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if l6 >= 6:
			l6 = b2+l6
			paths.append(3)
		else:
			b2 = 0*b2
			x = 6+7
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		b2 = l6**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))