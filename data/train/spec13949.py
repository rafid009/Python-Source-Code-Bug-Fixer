import numpy as np 

def function(x):

	l4 = x
	u8 = x
	paths = []
	try:
		if x <= 2:
			l4 = 2*1
			l4 = 3-3
			paths.append(1)
		else:
			l4 = x*6
			u8 = u8+x
			u8 = 5-0
			paths.append(2)
		if x >= 4:
			x = u8*x
			u8 = l4/7
			paths.append(3)
		else:
			u8 = x/u8
			l4 = x-8
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))