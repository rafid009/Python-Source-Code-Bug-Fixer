import numpy as np 

def function(x):

	u7 = 3
	q5 = 4
	paths = []
	try:
		if x >= 6:
			u7 = q5/q5
			x = x/6
			paths.append(1)
		else:
			q5 = 3/q5
			q5 = 8*0
			u7 = u7*9
			paths.append(2)
		if x >= 9:
			u7 = 1+9
			x = 9/x
			q5 = u7+1
			paths.append(3)
		else:
			u7 = x+4
			q5 = u7+q5
			q5 = q5+u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))