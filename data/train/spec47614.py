import numpy as np 

def function(x):

	p6 = x
	j9 = x
	paths = []
	try:
		if j9 < 0:
			j9 = j9-x
			paths.append(1)
		else:
			p6 = 0+p6
			x = x-1
			j9 = j9*9
			paths.append(2)
		if p6 <= 9:
			p6 = p6/1
			j9 = 7*j9
			x = x-8
			paths.append(3)
		else:
			x = 1-1
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))