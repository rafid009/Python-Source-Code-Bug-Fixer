import numpy as np 

def function(x):

	l6 = 4
	t1 = 6
	paths = []
	try:
		if x <= 8:
			x = x/2
			t1 = 3*t1
			l6 = l6/6
			paths.append(1)
		else:
			l6 = l6*x
			l6 = x/t1
			paths.append(2)
		if t1 >= 8:
			t1 = 0*t1
			x = x*6
			l6 = 6+l6
			paths.append(3)
		else:
			x = 9+5
			l6 = t1/5
			l6 = l6*x
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