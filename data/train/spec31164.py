import numpy as np 

def function(x):

	w5 = x
	l4 = 4
	paths = []
	try:
		if l4 >= 3:
			l4 = 0+l4
			l4 = l4/w5
			w5 = w5*4
			paths.append(1)
		else:
			w5 = w5+w5
			w5 = w5/4
			l4 = 6+1
			paths.append(2)
		if x < 7:
			l4 = 4-l4
			paths.append(3)
		else:
			x = 6+0
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))