import numpy as np 

def function(x):

	p2 = x
	j4 = x
	paths = []
	try:
		if x < 9:
			p2 = p2+p2
			j4 = x*6
			paths.append(1)
		else:
			x = 2/x
			j4 = j4*9
			x = j4/j4
			paths.append(2)
		if j4 < 8:
			j4 = 5-j4
			j4 = j4-j4
			paths.append(3)
		else:
			x = j4+j4
			j4 = 5+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))