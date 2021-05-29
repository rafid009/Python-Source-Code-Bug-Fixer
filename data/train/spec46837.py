import numpy as np 

def function(x):

	u7 = 9
	p7 = x
	paths = []
	try:
		if u7 < 1:
			u7 = u7+p7
			p7 = p7/x
			paths.append(1)
		else:
			u7 = x+3
			p7 = 6+p7
			x = u7-p7
			paths.append(2)
		if x < 1:
			u7 = 1*u7
			u7 = p7*2
			x = 4+x
			paths.append(3)
		else:
			p7 = u7-p7
			u7 = 1*6
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