import numpy as np 

def function(x):

	p3 = x
	p6 = 6
	paths = []
	try:
		if p3 <= 9:
			p6 = 8+x
			p6 = p3/p3
			paths.append(1)
		else:
			p3 = p3/5
			x = x*p6
			p6 = p6*5
			paths.append(2)
		if x < 6:
			x = x*6
			x = x+9
			paths.append(3)
		else:
			p3 = p3-6
			x = x+x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))