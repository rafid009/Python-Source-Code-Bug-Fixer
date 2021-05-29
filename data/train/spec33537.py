import numpy as np 

def function(x):

	i1 = 5
	t2 = 5
	x = 5
	paths = []
	try:
		if x <= 4:
			i1 = 7-i1
			x = 0-x
			paths.append(1)
		else:
			t2 = 3/t2
			i1 = 2-i1
			x = 3*7
			paths.append(2)
		if x >= 5:
			i1 = i1-x
			x = x*4
			paths.append(3)
		else:
			t2 = t2+i1
			t2 = 2+i1
			x = i1/x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))