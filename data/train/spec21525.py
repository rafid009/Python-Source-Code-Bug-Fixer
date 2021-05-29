import numpy as np 

def function(x):

	p8 = 3
	u3 = x
	paths = []
	try:
		if x < 6:
			u3 = p8+p8
			u3 = x-1
			p8 = 0-p8
			paths.append(1)
		else:
			u3 = u3+x
			paths.append(2)
		if x < 9:
			x = 3-x
			paths.append(3)
		else:
			x = x/1
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