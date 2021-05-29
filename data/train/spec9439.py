import numpy as np 

def function(x):

	n6 = x
	q3 = 8
	paths = []
	try:
		if n6 >= 9:
			n6 = n6*7
			x = 0/x
			n6 = 3*2
			paths.append(1)
		else:
			q3 = x*1
			n6 = x/q3
			n6 = n6/5
			paths.append(2)
		if x <= 3:
			x = 5-7
			q3 = 3/n6
			q3 = q3+8
			paths.append(3)
		else:
			q3 = n6-6
			q3 = q3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))