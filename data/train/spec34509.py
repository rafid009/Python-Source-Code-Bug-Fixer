import numpy as np 

def function(x):

	u7 = 8
	p2 = x
	paths = []
	try:
		if u7 <= 4:
			x = 3+x
			p2 = 2/p2
			paths.append(1)
		else:
			u7 = p2/8
			x = p2-7
			paths.append(2)
		if u7 >= 9:
			p2 = 4+7
			u7 = x*8
			paths.append(3)
		else:
			u7 = u7-x
			u7 = u7/7
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		u7 = p2**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))