import numpy as np 

def function(x):

	l2 = 6
	y8 = x
	paths = []
	try:
		if y8 > 4:
			l2 = 8*l2
			x = x-x
			y8 = y8*5
			paths.append(1)
		else:
			l2 = x+5
			paths.append(2)
		if x <= 9:
			x = x+3
			l2 = l2/2
			paths.append(3)
		else:
			x = 5/l2
			x = x*0
			y8 = 7+9
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))