import numpy as np 

def function(x):

	l7 = 9
	d5 = x
	x = x
	paths = []
	try:
		if l7 < 2:
			x = 8*x
			l7 = l7/6
			d5 = x*l7
			paths.append(1)
		else:
			x = x+d5
			l7 = x/5
			paths.append(2)
		if x >= 8:
			x = d5+0
			d5 = l7*d5
			l7 = l7/2
			paths.append(3)
		else:
			x = 7/x
			l7 = x/4
			l7 = 7/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))