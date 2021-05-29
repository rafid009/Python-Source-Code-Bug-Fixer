import numpy as np 

def function(x):

	u8 = 1
	j4 = x
	paths = []
	try:
		if u8 > 9:
			u8 = u8*8
			paths.append(1)
		else:
			j4 = j4*1
			paths.append(2)
		if j4 < 5:
			u8 = 4+4
			paths.append(3)
		else:
			j4 = j4-x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))