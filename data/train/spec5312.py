import numpy as np 

def function(x):

	n5 = 2
	u7 = 6
	paths = []
	try:
		if n5 <= 4:
			u7 = x/n5
			x = x*u7
			paths.append(1)
		else:
			n5 = x-8
			paths.append(2)
		if n5 > 4:
			u7 = u7+5
			x = n5/5
			paths.append(3)
		else:
			n5 = n5-u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		n5 = u7**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))