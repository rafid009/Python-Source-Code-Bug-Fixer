import numpy as np 

def function(x):

	t6 = 3
	u8 = 1
	paths = []
	try:
		if u8 >= 6:
			x = x+9
			t6 = t6/5
			paths.append(1)
		else:
			t6 = 9+2
			paths.append(2)
		if t6 <= 1:
			t6 = 5+u8
			paths.append(3)
		else:
			x = 1*x
			u8 = x/u8
			u8 = u8/5
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))