import numpy as np 

def function(x):

	y5 = 3
	l5 = x
	paths = []
	try:
		if y5 >= 9:
			x = x+9
			paths.append(1)
		else:
			x = x+3
			y5 = x/y5
			paths.append(2)
		if y5 > 7:
			l5 = 4/l5
			l5 = 3*4
			l5 = 6+6
			paths.append(3)
		else:
			l5 = 5*l5
			y5 = y5*2
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))