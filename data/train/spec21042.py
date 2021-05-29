import numpy as np 

def function(x):

	t5 = 2
	l6 = x
	x = x
	paths = []
	try:
		if l6 <= 1:
			t5 = l6/3
			paths.append(1)
		else:
			l6 = 6-x
			paths.append(2)
		if l6 < 3:
			x = x*4
			paths.append(3)
		else:
			x = 5+x
			l6 = 7*l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))