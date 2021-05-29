import numpy as np 

def function(x):

	e6 = 2
	u7 = x
	paths = []
	try:
		if u7 <= 4:
			u7 = u7-9
			x = x*0
			u7 = u7*8
			paths.append(1)
		else:
			e6 = u7+u7
			u7 = 9*u7
			e6 = 2/e6
			paths.append(2)
		if u7 >= 1:
			u7 = u7/1
			x = 2/x
			x = u7*x
			paths.append(3)
		else:
			e6 = u7/9
			u7 = 7+u7
			u7 = 2/u7
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))