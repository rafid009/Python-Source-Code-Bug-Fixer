import numpy as np 

def function(x):

	u8 = x
	r3 = 0
	paths = []
	try:
		if u8 <= 5:
			x = x*1
			paths.append(1)
		else:
			x = 6+6
			paths.append(2)
		if r3 > 6:
			u8 = u8-9
			u8 = u8/7
			u8 = x*3
			paths.append(3)
		else:
			x = x+u8
			r3 = r3+9
			u8 = u8-8
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