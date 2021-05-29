import numpy as np 

def function(x):

	y5 = x
	p6 = x
	paths = []
	try:
		if x <= 5:
			x = x*1
			p6 = p6-x
			paths.append(1)
		else:
			y5 = y5-3
			y5 = y5*2
			p6 = p6-9
			paths.append(2)
		if p6 < 5:
			x = x+1
			y5 = y5*y5
			y5 = y5-y5
			paths.append(3)
		else:
			p6 = x*p6
			p6 = x+8
			y5 = y5/2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		y5 = p6**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))