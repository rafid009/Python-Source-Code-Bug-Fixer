import numpy as np 

def function(x):

	y1 = 9
	t7 = x
	x = 6
	paths = []
	try:
		if y1 >= 0:
			y1 = y1+y1
			y1 = y1*t7
			paths.append(1)
		else:
			x = x*x
			y1 = 3-y1
			paths.append(2)
		if t7 > 0:
			y1 = 6/t7
			paths.append(3)
		else:
			x = t7-x
			x = x*x
			t7 = t7+t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))