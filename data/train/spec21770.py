import numpy as np 

def function(x):

	y1 = x
	t3 = 0
	paths = []
	try:
		if x > 7:
			y1 = y1+9
			y1 = 5/y1
			paths.append(1)
		else:
			x = 3-x
			t3 = t3-6
			paths.append(2)
		if t3 < 5:
			x = 1*x
			x = y1*5
			paths.append(3)
		else:
			y1 = y1+y1
			y1 = 5/4
			y1 = 0+6
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		t3 = y1**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))