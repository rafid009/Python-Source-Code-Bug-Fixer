import numpy as np 

def function(x):

	p9 = 7
	r1 = x
	paths = []
	try:
		if p9 >= 0:
			x = p9*r1
			x = 3/9
			paths.append(1)
		else:
			r1 = p9+9
			x = x-p9
			p9 = p9*4
			paths.append(2)
		if p9 > 2:
			x = 9-x
			p9 = 4-x
			r1 = 8+r1
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))