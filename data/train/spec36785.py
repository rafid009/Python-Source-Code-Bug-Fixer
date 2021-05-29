import numpy as np 

def function(x):

	p1 = 8
	y4 = 6
	paths = []
	try:
		if x > 5:
			y4 = y4+3
			paths.append(1)
		else:
			x = 6*2
			y4 = x+y4
			paths.append(2)
		if y4 >= 4:
			x = x*5
			y4 = y4*1
			p1 = 3-9
			paths.append(3)
		else:
			x = 8/x
			x = 1*x
			p1 = p1*p1
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