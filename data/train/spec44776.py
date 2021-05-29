import numpy as np 

def function(x):

	t7 = 6
	l7 = 6
	x = x
	paths = []
	try:
		if t7 >= 7:
			t7 = t7+9
			t7 = t7/x
			t7 = t7/5
			paths.append(1)
		else:
			l7 = 8/l7
			paths.append(2)
		if l7 < 7:
			t7 = t7+6
			l7 = l7*x
			t7 = t7/9
			paths.append(3)
		else:
			l7 = t7*t7
			x = x*1
			t7 = 2/t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))