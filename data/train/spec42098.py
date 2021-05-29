import numpy as np 

def function(x):

	u7 = 4
	p4 = x
	paths = []
	try:
		if u7 >= 3:
			x = x+p4
			paths.append(1)
		else:
			p4 = 9+2
			x = x+7
			paths.append(2)
		if u7 <= 7:
			x = p4-9
			x = x*8
			p4 = p4-9
			paths.append(3)
		else:
			p4 = 9/1
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		u7 = p4**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))