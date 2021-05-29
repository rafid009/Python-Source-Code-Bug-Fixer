import numpy as np 

def function(x):

	p1 = 9
	r4 = x
	paths = []
	try:
		if x > 7:
			x = 7*1
			r4 = 0-x
			r4 = p1-r4
			paths.append(1)
		else:
			p1 = 4-p1
			x = r4*9
			paths.append(2)
		if x < 4:
			r4 = r4+6
			x = 7/x
			x = 7+x
			paths.append(3)
		else:
			p1 = p1/2
			p1 = p1/1
			x = x/r4
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