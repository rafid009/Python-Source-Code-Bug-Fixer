import numpy as np 

def function(x):

	p9 = 2
	q3 = x
	paths = []
	try:
		if x >= 5:
			q3 = q3*4
			x = x+q3
			paths.append(1)
		else:
			q3 = q3/3
			paths.append(2)
		if p9 >= 9:
			p9 = x-p9
			p9 = 0+p9
			x = x+1
			paths.append(3)
		else:
			q3 = 5-8
			x = 7*x
			p9 = 0-p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))