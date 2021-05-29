import numpy as np 

def function(x):

	p2 = 8
	u7 = x
	paths = []
	try:
		if u7 <= 6:
			p2 = u7-2
			u7 = 2+u7
			x = x-1
			paths.append(1)
		else:
			p2 = p2-u7
			paths.append(2)
		if p2 >= 3:
			p2 = 9*u7
			p2 = p2-7
			p2 = 0*6
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))