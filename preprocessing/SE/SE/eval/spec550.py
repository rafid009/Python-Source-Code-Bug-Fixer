import numpy as np 

def function(x):

	p1 = 1
	u8 = 2
	paths = []
	try:
		if u8 > 4:
			p1 = u8*u8
			u8 = u8-u8
			paths.append(1)
		else:
			x = u8-p1
			u8 = u8*1
			paths.append(2)
		if x > 3:
			x = x*x
			u8 = u8+p1
			u8 = u8/u8
			paths.append(3)
		else:
			u8 = 2-9
			p1 = p1-3
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))