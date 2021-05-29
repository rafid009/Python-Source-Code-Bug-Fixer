import numpy as np 

def function(x):

	l4 = 2
	u8 = 0
	paths = []
	try:
		if u8 > 6:
			l4 = l4+7
			paths.append(1)
		else:
			u8 = u8/1
			x = x/l4
			l4 = 3-l4
			paths.append(2)
		if l4 <= 7:
			x = x*4
			paths.append(3)
		else:
			u8 = 7+1
			l4 = l4+l4
			x = l4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))