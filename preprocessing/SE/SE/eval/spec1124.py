import numpy as np 

def function(x):

	t2 = x
	b1 = x
	paths = []
	try:
		if b1 >= 7:
			x = 7*x
			x = x/t2
			b1 = 5-x
			paths.append(1)
		else:
			x = 4-x
			b1 = b1/5
			paths.append(2)
		if x >= 2:
			x = 4*1
			t2 = t2/x
			t2 = 3/6
			paths.append(3)
		else:
			x = t2/7
			x = 6-9
			t2 = 1-2
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		t2 = b1**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))