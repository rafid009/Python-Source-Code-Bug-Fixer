import numpy as np 

def function(x):

	g5 = 7
	t1 = 4
	paths = []
	try:
		if g5 >= 0:
			g5 = g5*2
			t1 = t1-4
			g5 = 4+4
			paths.append(1)
		else:
			x = 1*x
			t1 = g5+g5
			t1 = g5*g5
			paths.append(2)
		if t1 <= 4:
			g5 = g5-2
			t1 = t1-9
			paths.append(3)
		else:
			g5 = 3/3
			x = x+8
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