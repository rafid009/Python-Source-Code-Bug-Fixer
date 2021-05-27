import numpy as np 

def function(x):

	t9 = x
	l8 = 2
	x = 4
	paths = []
	try:
		if l8 >= 0:
			t9 = 3/t9
			t9 = l8-5
			t9 = t9/8
			paths.append(1)
		else:
			x = x/9
			l8 = l8/3
			l8 = l8+7
			paths.append(2)
		if x <= 9:
			l8 = l8/7
			paths.append(3)
		else:
			t9 = 5*t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		l8 = t9**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))