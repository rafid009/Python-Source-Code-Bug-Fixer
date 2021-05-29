import numpy as np 

def function(x):

	p8 = 7
	q3 = x
	paths = []
	try:
		if p8 < 3:
			p8 = 3+2
			paths.append(1)
		else:
			x = 4/x
			q3 = q3*x
			p8 = q3+9
			paths.append(2)
		if x < 6:
			q3 = q3/4
			q3 = 9-p8
			paths.append(3)
		else:
			x = x+2
			p8 = 6-p8
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		p8 = q3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))