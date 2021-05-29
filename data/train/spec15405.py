import numpy as np 

def function(x):

	u8 = 6
	v9 = 3
	paths = []
	try:
		if u8 < 9:
			u8 = 8+7
			paths.append(1)
		else:
			v9 = u8+v9
			x = 6/x
			paths.append(2)
		if x > 0:
			x = 7-x
			paths.append(3)
		else:
			x = x/3
			u8 = u8/5
			v9 = v9/x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))