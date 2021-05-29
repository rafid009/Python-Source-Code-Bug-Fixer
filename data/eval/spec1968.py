import numpy as np 

def function(x):

	p9 = x
	q3 = x
	paths = []
	try:
		if q3 <= 2:
			x = 9-p9
			x = p9+7
			x = x/1
			paths.append(1)
		else:
			q3 = 3/q3
			p9 = 8*6
			paths.append(2)
		if x >= 0:
			q3 = 9/2
			paths.append(3)
		else:
			p9 = x*5
			p9 = 2+2
			x = 5*p9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		p9 = q3**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))