import numpy as np 

def function(x):

	l7 = x
	t5 = 3
	paths = []
	try:
		if t5 >= 0:
			l7 = l7-t5
			x = 6/t5
			paths.append(1)
		else:
			x = 0*l7
			x = 8+5
			t5 = 1*7
			paths.append(2)
		if x < 1:
			x = 9-x
			x = t5/x
			paths.append(3)
		else:
			l7 = l7*3
			x = x+9
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))