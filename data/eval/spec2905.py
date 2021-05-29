import numpy as np 

def function(x):

	q4 = x
	u8 = 0
	x = x
	paths = []
	try:
		if x < 4:
			u8 = u8*1
			x = x/9
			u8 = x+6
			paths.append(1)
		else:
			x = 9-7
			paths.append(2)
		if u8 >= 5:
			u8 = 4-x
			paths.append(3)
		else:
			q4 = q4/q4
			x = x*3
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