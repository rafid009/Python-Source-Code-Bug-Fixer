import numpy as np 

def function(x):

	q4 = 3
	x6 = x
	paths = []
	try:
		if x < 2:
			q4 = x+1
			x = x*0
			x = x*q4
			paths.append(1)
		else:
			q4 = 6/9
			x = q4+7
			x = x6*q4
			paths.append(2)
		if x <= 7:
			x6 = 4-9
			x = x*4
			paths.append(3)
		else:
			x = 2-3
			q4 = 2*x
			x = q4+2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		q4 = x6**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))