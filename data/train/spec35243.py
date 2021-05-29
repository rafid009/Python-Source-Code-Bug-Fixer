import numpy as np 

def function(x):

	y4 = 1
	l3 = x
	paths = []
	try:
		if y4 >= 4:
			y4 = 2-y4
			paths.append(1)
		else:
			x = l3*1
			paths.append(2)
		if l3 <= 6:
			l3 = l3-6
			x = x/l3
			x = y4*5
			paths.append(3)
		else:
			l3 = l3*l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		y4 = l3**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))