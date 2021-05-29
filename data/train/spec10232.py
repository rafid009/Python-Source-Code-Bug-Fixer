import numpy as np 

def function(x):

	n7 = 7
	u8 = x
	paths = []
	try:
		if u8 > 8:
			x = 9*x
			x = x*8
			paths.append(1)
		else:
			n7 = 8+1
			x = u8*0
			paths.append(2)
		if u8 <= 2:
			n7 = 4*n7
			n7 = x*9
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		n7 = u8**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))