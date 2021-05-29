import numpy as np 

def function(x):

	t7 = x
	l5 = 8
	x = 3
	paths = []
	try:
		if t7 <= 7:
			t7 = l5+2
			paths.append(1)
		else:
			x = x*l5
			x = x+6
			l5 = 3-l5
			paths.append(2)
		if t7 < 7:
			x = 3-x
			paths.append(3)
		else:
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))