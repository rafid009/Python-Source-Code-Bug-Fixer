import numpy as np 

def function(x):

	n2 = 4
	t1 = 5
	paths = []
	try:
		if t1 < 5:
			x = x*x
			x = x*7
			paths.append(1)
		else:
			t1 = 2-n2
			x = x/3
			paths.append(2)
		if x > 5:
			x = t1-0
			paths.append(3)
		else:
			t1 = 7-0
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