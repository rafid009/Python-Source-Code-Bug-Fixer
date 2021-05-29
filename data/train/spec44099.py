import numpy as np 

def function(x):

	p6 = 4
	u3 = 6
	x = x
	paths = []
	try:
		if x >= 6:
			p6 = 3+p6
			x = x*3
			paths.append(1)
		else:
			u3 = x+8
			p6 = p6-u3
			paths.append(2)
		if u3 >= 6:
			p6 = p6-2
			paths.append(3)
		else:
			p6 = p6/p6
			u3 = 6+x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		p6 = u3**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))