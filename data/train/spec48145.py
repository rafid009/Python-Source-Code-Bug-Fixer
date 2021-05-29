import numpy as np 

def function(x):

	t3 = 1
	y6 = x
	x = 5
	paths = []
	try:
		if x <= 7:
			y6 = 7*y6
			y6 = y6*8
			t3 = y6-y6
			paths.append(1)
		else:
			x = x+9
			y6 = y6*y6
			paths.append(2)
		if y6 <= 7:
			t3 = t3-5
			paths.append(3)
		else:
			x = 0-9
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		t3 = y6**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))