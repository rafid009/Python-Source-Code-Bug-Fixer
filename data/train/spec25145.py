import numpy as np 

def function(x):

	l9 = 1
	t9 = 5
	paths = []
	try:
		if x > 5:
			x = 8+7
			paths.append(1)
		else:
			t9 = t9*4
			paths.append(2)
		if x > 5:
			x = x*6
			x = 5*t9
			l9 = l9-9
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		t9 = l9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))