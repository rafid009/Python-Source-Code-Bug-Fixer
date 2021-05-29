import numpy as np 

def function(x):

	p3 = 7
	n7 = 6
	paths = []
	try:
		if p3 <= 3:
			x = n7/2
			paths.append(1)
		else:
			p3 = x-p3
			n7 = n7-p3
			p3 = p3*6
			paths.append(2)
		if n7 >= 7:
			p3 = 0+7
			p3 = 8+8
			paths.append(3)
		else:
			n7 = n7+3
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