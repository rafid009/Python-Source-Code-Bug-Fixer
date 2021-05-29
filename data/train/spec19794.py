import numpy as np 

def function(x):

	y6 = x
	t9 = x
	paths = []
	try:
		if y6 <= 2:
			y6 = y6-5
			x = 2-x
			paths.append(1)
		else:
			t9 = 7*1
			t9 = 1/t9
			y6 = 8+y6
			paths.append(2)
		if x > 4:
			t9 = t9/t9
			paths.append(3)
		else:
			x = x+2
			t9 = t9/3
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		t9 = y6**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))