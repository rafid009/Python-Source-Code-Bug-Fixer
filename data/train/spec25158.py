import numpy as np 

def function(x):

	d4 = 6
	l9 = 8
	paths = []
	try:
		if d4 >= 6:
			l9 = 5-l9
			paths.append(1)
		else:
			d4 = l9+4
			l9 = l9/l9
			x = x*l9
			paths.append(2)
		if x <= 2:
			x = x+5
			l9 = d4+l9
			d4 = d4-1
			paths.append(3)
		else:
			x = l9+x
			l9 = l9/6
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))