import numpy as np 

def function(x):

	q8 = 2
	p8 = 2
	paths = []
	try:
		if x < 1:
			x = 1+x
			q8 = 5+q8
			paths.append(1)
		else:
			q8 = 6-9
			p8 = 4/7
			x = x+x
			paths.append(2)
		if q8 <= 5:
			x = 2/p8
			q8 = x-0
			p8 = x*p8
			paths.append(3)
		else:
			q8 = x+p8
			p8 = p8/2
			p8 = 0+p8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))