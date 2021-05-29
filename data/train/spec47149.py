import numpy as np 

def function(x):

	t1 = 4
	q6 = x
	paths = []
	try:
		if t1 >= 2:
			q6 = 3-5
			t1 = t1-4
			paths.append(1)
		else:
			t1 = 9*2
			q6 = 2/3
			paths.append(2)
		if t1 <= 3:
			t1 = 3+t1
			t1 = t1-8
			paths.append(3)
		else:
			x = 3+3
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))