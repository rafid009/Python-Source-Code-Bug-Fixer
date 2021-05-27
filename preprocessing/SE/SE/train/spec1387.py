import numpy as np 

def function(x):

	i5 = 2
	l5 = x
	paths = []
	try:
		if l5 <= 1:
			x = l5/i5
			l5 = l5/8
			x = x*7
			paths.append(1)
		else:
			i5 = i5*4
			l5 = l5*i5
			paths.append(2)
		if x < 8:
			x = 3+x
			l5 = l5/l5
			x = x-8
			paths.append(3)
		else:
			l5 = l5-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))