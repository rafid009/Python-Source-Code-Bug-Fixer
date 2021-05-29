import numpy as np 

def function(x):

	p7 = x
	q5 = x
	paths = []
	try:
		if q5 > 3:
			x = 0/x
			q5 = q5+q5
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x < 8:
			q5 = 2-q5
			x = 8*q5
			paths.append(3)
		else:
			p7 = 0*0
			q5 = 1*q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))