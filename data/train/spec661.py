import numpy as np 

def function(x):

	l0 = x
	f3 = 7
	paths = []
	try:
		if x >= 2:
			l0 = 2/l0
			paths.append(1)
		else:
			x = 4+9
			f3 = 5*2
			x = x+5
			paths.append(2)
		if x <= 5:
			x = 7/8
			paths.append(3)
		else:
			x = 9/1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))