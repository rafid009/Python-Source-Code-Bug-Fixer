import numpy as np 

def function(x):

	g2 = 6
	u8 = 8
	paths = []
	try:
		if g2 >= 7:
			g2 = 5*4
			u8 = 4*8
			paths.append(1)
		else:
			g2 = 2+g2
			u8 = g2*0
			x = u8+x
			paths.append(2)
		if x <= 2:
			u8 = u8-1
			x = x/x
			paths.append(3)
		else:
			u8 = 6-u8
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