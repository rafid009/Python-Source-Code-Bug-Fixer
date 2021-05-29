import numpy as np 

def function(x):

	t7 = x
	l9 = x
	paths = []
	try:
		if x > 6:
			t7 = t7*8
			paths.append(1)
		else:
			x = x/7
			x = 1+t7
			paths.append(2)
		if t7 > 6:
			t7 = 2*t7
			t7 = x+5
			l9 = 6/4
			paths.append(3)
		else:
			x = x*2
			x = t7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))