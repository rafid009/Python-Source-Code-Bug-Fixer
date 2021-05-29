import numpy as np 

def function(x):

	u3 = x
	u8 = x
	paths = []
	try:
		if u8 > 4:
			u8 = 6+u8
			x = x/4
			paths.append(1)
		else:
			x = u8+9
			u3 = 8+u3
			u3 = 2-u3
			paths.append(2)
		if u8 <= 5:
			u8 = 9-u8
			x = 4+2
			x = x*5
			paths.append(3)
		else:
			u8 = u8-7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u8 = u3**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))