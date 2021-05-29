import numpy as np 

def function(x):

	l4 = x
	j4 = x
	paths = []
	try:
		if x <= 4:
			x = x/1
			paths.append(1)
		else:
			j4 = 0/8
			j4 = j4*7
			paths.append(2)
		if l4 <= 3:
			l4 = l4*x
			paths.append(3)
		else:
			x = l4*x
			l4 = 2/l4
			l4 = 2-6
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))