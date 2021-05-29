import numpy as np 

def function(x):

	t5 = 7
	l8 = 7
	paths = []
	try:
		if t5 < 2:
			t5 = t5+7
			x = 9/5
			t5 = 4*0
			paths.append(1)
		else:
			t5 = 4/t5
			paths.append(2)
		if t5 >= 9:
			x = 4+x
			l8 = x+l8
			t5 = t5+6
			paths.append(3)
		else:
			l8 = l8/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))