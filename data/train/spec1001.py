import numpy as np 

def function(x):

	p9 = x
	j4 = x
	paths = []
	try:
		if x <= 8:
			j4 = j4/5
			x = 3*9
			p9 = 2/p9
			paths.append(1)
		else:
			x = 7-x
			j4 = j4/p9
			p9 = 8/p9
			paths.append(2)
		if p9 <= 2:
			x = x+7
			p9 = 6/p9
			x = x-5
			paths.append(3)
		else:
			j4 = 2-j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))