import numpy as np 

def function(x):

	t6 = 6
	y1 = 0
	paths = []
	try:
		if y1 <= 5:
			y1 = 3-y1
			y1 = y1-y1
			y1 = y1*9
			paths.append(1)
		else:
			y1 = y1/x
			t6 = t6*0
			y1 = 5+1
			paths.append(2)
		if t6 > 5:
			t6 = 7-t6
			y1 = 2-6
			x = x/5
			paths.append(3)
		else:
			t6 = t6/y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))