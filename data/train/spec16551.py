import numpy as np 

def function(x):

	y4 = x
	p3 = x
	paths = []
	try:
		if p3 >= 8:
			p3 = p3-y4
			paths.append(1)
		else:
			p3 = p3-8
			y4 = 4*3
			paths.append(2)
		if y4 >= 6:
			p3 = p3/5
			p3 = p3-7
			p3 = p3+1
			paths.append(3)
		else:
			x = x-p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))