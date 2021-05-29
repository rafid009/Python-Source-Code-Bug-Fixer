import numpy as np 

def function(x):

	u4 = x
	f6 = 3
	paths = []
	try:
		if x > 6:
			f6 = f6-5
			x = 3+x
			paths.append(1)
		else:
			x = 2*0
			u4 = 0+u4
			paths.append(2)
		if f6 <= 6:
			x = 7+x
			paths.append(3)
		else:
			f6 = f6-1
			f6 = 8*4
			x = x+8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))