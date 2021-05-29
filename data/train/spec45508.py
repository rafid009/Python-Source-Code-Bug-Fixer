import numpy as np 

def function(x):

	l4 = 9
	k6 = x
	paths = []
	try:
		if k6 <= 9:
			l4 = 6/9
			k6 = k6-0
			k6 = x*9
			paths.append(1)
		else:
			k6 = x/k6
			paths.append(2)
		if k6 <= 8:
			k6 = k6+5
			l4 = l4-4
			x = 7-1
			paths.append(3)
		else:
			l4 = l4-9
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))