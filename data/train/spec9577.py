import numpy as np 

def function(x):

	l5 = 3
	a1 = x
	paths = []
	try:
		if x <= 3:
			l5 = a1/x
			paths.append(1)
		else:
			l5 = 5/3
			l5 = l5/5
			l5 = l5-1
			paths.append(2)
		if x > 9:
			a1 = a1-2
			x = 1/x
			x = 4*3
			paths.append(3)
		else:
			x = x/1
			x = a1-x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))