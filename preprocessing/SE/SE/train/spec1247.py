import numpy as np 

def function(x):

	l4 = x
	t3 = x
	paths = []
	try:
		if x > 2:
			l4 = l4/7
			paths.append(1)
		else:
			x = x/t3
			l4 = 7/l4
			paths.append(2)
		if x >= 3:
			t3 = 1-t3
			paths.append(3)
		else:
			x = x+7
			l4 = x+l4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		l4 = t3**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))