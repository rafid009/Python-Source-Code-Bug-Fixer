import numpy as np 

def function(x):

	d8 = 8
	l9 = 6
	paths = []
	try:
		if l9 > 9:
			x = 4*x
			x = x*d8
			l9 = l9+1
			paths.append(1)
		else:
			l9 = l9-8
			l9 = l9/x
			x = d8-x
			paths.append(2)
		if l9 <= 5:
			l9 = 7-x
			paths.append(3)
		else:
			l9 = x/l9
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))