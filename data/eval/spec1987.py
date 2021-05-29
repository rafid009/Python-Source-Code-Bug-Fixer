import numpy as np 

def function(x):

	f9 = x
	l1 = 4
	paths = []
	try:
		if x > 5:
			f9 = 1*f9
			l1 = l1*f9
			paths.append(1)
		else:
			f9 = 5-7
			paths.append(2)
		if l1 < 5:
			f9 = f9-8
			x = 6-l1
			paths.append(3)
		else:
			x = 8-x
			l1 = l1-l1
			l1 = l1/7
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))