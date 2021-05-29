import numpy as np 

def function(x):

	l6 = 5
	u8 = 1
	paths = []
	try:
		if u8 > 0:
			u8 = l6+1
			paths.append(1)
		else:
			l6 = l6/l6
			l6 = 6*8
			paths.append(2)
		if u8 <= 3:
			l6 = l6-7
			u8 = l6+u8
			paths.append(3)
		else:
			u8 = l6-u8
			u8 = 6*u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		l6 = u8**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))