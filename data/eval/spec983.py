import numpy as np 

def function(x):

	u4 = x
	p8 = 0
	x = x
	paths = []
	try:
		if p8 > 7:
			x = x/1
			paths.append(1)
		else:
			u4 = u4+3
			paths.append(2)
		if u4 <= 6:
			u4 = x*u4
			u4 = u4-4
			paths.append(3)
		else:
			u4 = u4+1
			p8 = 6+p8
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