import numpy as np 

def function(x):

	y5 = x
	p7 = 2
	paths = []
	try:
		if x <= 8:
			x = x*1
			paths.append(1)
		else:
			y5 = y5*7
			p7 = p7*8
			paths.append(2)
		if y5 <= 1:
			p7 = p7*1
			p7 = p7-4
			p7 = 2-p7
			paths.append(3)
		else:
			y5 = x*2
			x = y5/3
			x = x*5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))