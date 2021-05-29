import numpy as np 

def function(x):

	l4 = x
	t7 = 6
	paths = []
	try:
		if l4 <= 3:
			x = l4+7
			x = 6/x
			l4 = 4*3
			paths.append(1)
		else:
			l4 = l4/5
			paths.append(2)
		if l4 > 3:
			t7 = l4*t7
			l4 = x-t7
			t7 = l4+t7
			paths.append(3)
		else:
			t7 = 2/x
			x = x*1
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))