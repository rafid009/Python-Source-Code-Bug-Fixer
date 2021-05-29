import numpy as np 

def function(x):

	t3 = x
	l6 = 3
	paths = []
	try:
		if x >= 5:
			t3 = l6*7
			l6 = l6*6
			paths.append(1)
		else:
			t3 = t3*l6
			t3 = 5-t3
			paths.append(2)
		if l6 <= 6:
			x = x-4
			t3 = 3*t3
			paths.append(3)
		else:
			t3 = t3+8
			l6 = l6-2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))