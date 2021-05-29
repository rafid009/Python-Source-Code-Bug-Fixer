import numpy as np 

def function(x):

	u4 = 2
	p8 = x
	x = 9
	paths = []
	try:
		if p8 <= 8:
			u4 = u4*7
			paths.append(1)
		else:
			u4 = u4/3
			u4 = u4*6
			x = 5-x
			paths.append(2)
		if p8 <= 7:
			u4 = u4*x
			u4 = p8+6
			paths.append(3)
		else:
			u4 = 7+u4
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))