import numpy as np 

def function(x):

	p6 = x
	y1 = 5
	paths = []
	try:
		if x < 3:
			y1 = y1*2
			y1 = y1-7
			paths.append(1)
		else:
			x = x*p6
			p6 = y1+x
			p6 = 6/8
			paths.append(2)
		if x > 7:
			x = 9-7
			y1 = 9-y1
			paths.append(3)
		else:
			p6 = 0+p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		y1 = p6**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))