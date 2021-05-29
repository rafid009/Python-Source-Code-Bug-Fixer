import numpy as np 

def function(x):

	p7 = x
	q3 = 7
	paths = []
	try:
		if p7 <= 4:
			q3 = 6/q3
			x = 5+p7
			p7 = p7*2
			paths.append(1)
		else:
			x = 9+x
			x = x-9
			paths.append(2)
		if x > 0:
			q3 = 1-2
			paths.append(3)
		else:
			p7 = x-p7
			p7 = q3-p7
			q3 = 7/x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))