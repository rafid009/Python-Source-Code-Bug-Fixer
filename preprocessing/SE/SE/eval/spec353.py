import numpy as np 

def function(x):

	p8 = x
	p3 = x
	paths = []
	try:
		if p8 > 8:
			p8 = p8/p8
			paths.append(1)
		else:
			x = 5+7
			p3 = x/1
			p8 = x*p8
			paths.append(2)
		if x > 3:
			x = p3+9
			paths.append(3)
		else:
			p3 = 7+p8
			p8 = p8*3
			p3 = 7+6
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p3 = p8**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))