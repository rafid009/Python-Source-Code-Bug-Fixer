import numpy as np 

def function(x):

	j9 = 4
	p8 = x
	paths = []
	try:
		if p8 >= 3:
			x = 4+x
			x = x*j9
			paths.append(1)
		else:
			x = x-p8
			paths.append(2)
		if j9 <= 6:
			x = 0-x
			x = 0-1
			paths.append(3)
		else:
			x = 2-5
			p8 = p8/4
			j9 = j9*6
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))