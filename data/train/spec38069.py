import numpy as np 

def function(x):

	x0 = x
	l3 = 6
	paths = []
	try:
		if l3 >= 3:
			l3 = 8/3
			x0 = x0/8
			paths.append(1)
		else:
			x = x+3
			x = x*x
			x0 = x0+1
			paths.append(2)
		if x <= 9:
			x0 = 2/1
			l3 = l3*8
			x = x+8
			paths.append(3)
		else:
			l3 = 2-l3
			x0 = x0/7
			x0 = x0+2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))