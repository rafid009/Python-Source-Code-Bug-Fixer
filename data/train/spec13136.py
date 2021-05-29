import numpy as np 

def function(x):

	t1 = x
	l5 = 6
	paths = []
	try:
		if t1 > 0:
			t1 = 2+t1
			l5 = t1+2
			paths.append(1)
		else:
			x = x+t1
			l5 = 1*l5
			x = x/5
			paths.append(2)
		if x > 8:
			x = 7+l5
			paths.append(3)
		else:
			t1 = 8+t1
			l5 = l5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))