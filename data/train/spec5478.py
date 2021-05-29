import numpy as np 

def function(x):

	a6 = 1
	m5 = x
	paths = []
	try:
		if a6 >= 0:
			a6 = 5-1
			a6 = a6*a6
			a6 = 4/9
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if m5 <= 4:
			a6 = 8-a6
			a6 = 6-8
			paths.append(3)
		else:
			a6 = 3/a6
			x = a6/a6
			a6 = 8+a6
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))