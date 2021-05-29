import numpy as np 

def function(x):

	y1 = 6
	t2 = 4
	paths = []
	try:
		if y1 >= 5:
			x = x*1
			t2 = t2*4
			t2 = 9*t2
			paths.append(1)
		else:
			x = 8-8
			y1 = y1-7
			paths.append(2)
		if x <= 2:
			x = x+3
			paths.append(3)
		else:
			t2 = 7/9
			y1 = 1-3
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		t2 = y1**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))