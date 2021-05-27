import numpy as np 

def function(x):

	y4 = 2
	r1 = 4
	paths = []
	try:
		if x < 0:
			r1 = r1+y4
			r1 = r1-6
			x = x+1
			paths.append(1)
		else:
			x = 6*x
			r1 = r1+7
			paths.append(2)
		if y4 <= 1:
			x = x/y4
			y4 = y4*6
			y4 = 5+y4
			paths.append(3)
		else:
			y4 = 5-y4
			r1 = 1-9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		y4 = r1**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))