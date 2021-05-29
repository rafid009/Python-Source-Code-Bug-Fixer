import numpy as np 

def function(x):

	p7 = x
	k6 = 2
	paths = []
	try:
		if p7 > 4:
			p7 = 8*p7
			x = x-5
			x = x+p7
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if k6 <= 8:
			k6 = 8-k6
			paths.append(3)
		else:
			x = 6*p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))