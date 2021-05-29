import numpy as np 

def function(x):

	p7 = 2
	u8 = x
	paths = []
	try:
		if p7 < 3:
			p7 = p7*9
			p7 = 7/7
			p7 = 3/p7
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x <= 9:
			u8 = x/8
			paths.append(3)
		else:
			p7 = 4-3
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