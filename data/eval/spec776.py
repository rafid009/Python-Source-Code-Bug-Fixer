import numpy as np 

def function(x):

	u8 = x
	t2 = x
	paths = []
	try:
		if u8 >= 1:
			t2 = x*4
			x = x/7
			paths.append(1)
		else:
			x = 2*x
			u8 = 6/u8
			x = t2-x
			paths.append(2)
		if t2 < 4:
			x = 2+5
			paths.append(3)
		else:
			t2 = x-t2
			x = x*u8
			x = t2/x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		u8 = t2**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))