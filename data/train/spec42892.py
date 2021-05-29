import numpy as np 

def function(x):

	p6 = x
	y8 = x
	x = x
	paths = []
	try:
		if p6 < 3:
			y8 = y8-2
			x = x*9
			paths.append(1)
		else:
			p6 = p6/5
			x = 9*5
			p6 = p6-p6
			paths.append(2)
		if x < 5:
			y8 = y8+3
			paths.append(3)
		else:
			p6 = x*p6
			y8 = y8/9
			p6 = p6*p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		y8 = p6**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))