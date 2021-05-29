import numpy as np 

def function(x):

	u5 = 5
	q5 = x
	paths = []
	try:
		if x >= 6:
			q5 = q5/q5
			paths.append(1)
		else:
			u5 = u5*2
			x = x-1
			paths.append(2)
		if x < 1:
			q5 = x/q5
			u5 = x/3
			x = 9*x
			paths.append(3)
		else:
			q5 = q5+u5
			u5 = x-4
			x = x*5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		u5 = q5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))