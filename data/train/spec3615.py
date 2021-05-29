import numpy as np 

def function(x):

	l5 = x
	b7 = x
	paths = []
	try:
		if l5 < 5:
			x = x*l5
			x = x/b7
			b7 = b7/3
			paths.append(1)
		else:
			b7 = b7+b7
			b7 = l5+7
			x = x-7
			paths.append(2)
		if b7 > 4:
			x = 7-x
			l5 = 3-l5
			l5 = l5*b7
			paths.append(3)
		else:
			l5 = 0-0
			b7 = 2+b7
			l5 = 5*4
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))