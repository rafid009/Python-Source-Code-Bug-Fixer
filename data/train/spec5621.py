import numpy as np 

def function(x):

	v3 = 3
	u8 = 8
	paths = []
	try:
		if x <= 7:
			x = x-7
			x = 6+u8
			paths.append(1)
		else:
			v3 = 8+v3
			paths.append(2)
		if u8 > 3:
			v3 = v3-u8
			v3 = 5/v3
			paths.append(3)
		else:
			v3 = 0+v3
			v3 = 9*v3
			v3 = u8/v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))