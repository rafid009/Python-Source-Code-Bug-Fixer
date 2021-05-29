import numpy as np 

def function(x):

	l6 = 7
	f9 = x
	paths = []
	try:
		if f9 > 4:
			l6 = 4*7
			x = 6*7
			paths.append(1)
		else:
			l6 = l6*0
			x = 1+x
			paths.append(2)
		if x > 2:
			f9 = 5+f9
			paths.append(3)
		else:
			x = l6-5
			l6 = 9-l6
			x = x/f9
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