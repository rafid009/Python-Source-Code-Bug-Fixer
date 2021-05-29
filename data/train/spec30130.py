import numpy as np 

def function(x):

	t7 = x
	u8 = x
	paths = []
	try:
		if x >= 8:
			u8 = u8*4
			x = x/7
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if t7 > 5:
			t7 = 9/u8
			paths.append(3)
		else:
			u8 = 0-8
			u8 = 7*u8
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))