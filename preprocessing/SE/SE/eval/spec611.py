import numpy as np 

def function(x):

	u5 = 7
	p6 = 9
	paths = []
	try:
		if x > 2:
			u5 = 5/x
			x = x*5
			paths.append(1)
		else:
			x = x*u5
			u5 = u5-u5
			p6 = x+6
			paths.append(2)
		if u5 <= 9:
			p6 = u5-9
			paths.append(3)
		else:
			u5 = u5/5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		u5 = p6**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))