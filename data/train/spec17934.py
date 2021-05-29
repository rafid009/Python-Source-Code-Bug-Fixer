import numpy as np 

def function(x):

	x4 = x
	q5 = 6
	paths = []
	try:
		if x4 > 4:
			x4 = x4*0
			x4 = x4+4
			x = 8+q5
			paths.append(1)
		else:
			x = q5-x
			x4 = 2-x4
			q5 = q5/2
			paths.append(2)
		if x4 > 5:
			q5 = 5*q5
			x4 = x4+1
			paths.append(3)
		else:
			q5 = x+x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))