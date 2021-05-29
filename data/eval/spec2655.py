import numpy as np 

def function(x):

	t3 = 1
	l7 = 7
	paths = []
	try:
		if x < 8:
			t3 = t3+l7
			l7 = l7+6
			paths.append(1)
		else:
			x = 0-x
			l7 = 4+l7
			x = 4*1
			paths.append(2)
		if t3 < 0:
			x = 1-x
			l7 = x/t3
			t3 = t3*t3
			paths.append(3)
		else:
			l7 = l7*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))