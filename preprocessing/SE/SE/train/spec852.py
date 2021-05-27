import numpy as np 

def function(x):

	p7 = 5
	f4 = x
	paths = []
	try:
		if p7 >= 8:
			f4 = f4+7
			x = x*p7
			paths.append(1)
		else:
			p7 = p7*9
			paths.append(2)
		if p7 <= 6:
			x = 5-0
			paths.append(3)
		else:
			p7 = 2/f4
			f4 = f4+9
			f4 = f4+8
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