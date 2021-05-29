import numpy as np 

def function(x):

	u8 = 6
	v5 = 6
	paths = []
	try:
		if v5 < 3:
			v5 = u8/6
			paths.append(1)
		else:
			v5 = u8*v5
			v5 = x-u8
			u8 = 3+v5
			paths.append(2)
		if u8 > 6:
			x = 6-9
			u8 = u8*3
			paths.append(3)
		else:
			v5 = v5/5
			u8 = u8*u8
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))