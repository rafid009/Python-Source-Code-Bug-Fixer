import numpy as np 

def function(x):

	q5 = x
	a1 = 5
	paths = []
	try:
		if q5 > 6:
			x = x*3
			q5 = 0*9
			x = x*0
			paths.append(1)
		else:
			a1 = 2+a1
			q5 = q5-8
			q5 = q5/8
			paths.append(2)
		if q5 > 7:
			q5 = q5*q5
			q5 = 6/6
			x = x*x
			paths.append(3)
		else:
			q5 = q5*q5
			q5 = q5-2
			q5 = q5*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))