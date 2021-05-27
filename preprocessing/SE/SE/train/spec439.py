import numpy as np 

def function(x):

	f9 = 2
	l3 = x
	paths = []
	try:
		if x <= 4:
			l3 = 1-l3
			l3 = l3/9
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if l3 < 1:
			f9 = f9-7
			x = x-x
			f9 = 8-f9
			paths.append(3)
		else:
			l3 = 0+0
			l3 = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))