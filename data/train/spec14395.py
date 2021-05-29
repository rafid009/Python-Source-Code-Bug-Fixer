import numpy as np 

def function(x):

	t9 = x
	l4 = 7
	paths = []
	try:
		if x > 3:
			x = l4/4
			x = 6/3
			paths.append(1)
		else:
			t9 = 4+t9
			paths.append(2)
		if x <= 4:
			x = 3*x
			t9 = 6/t9
			paths.append(3)
		else:
			l4 = 2-1
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))