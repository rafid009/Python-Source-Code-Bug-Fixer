import numpy as np 

def function(x):

	u9 = x
	j7 = x
	paths = []
	try:
		if x > 0:
			u9 = 4*j7
			paths.append(1)
		else:
			j7 = j7*0
			paths.append(2)
		if j7 < 7:
			u9 = 8*u9
			j7 = j7-0
			u9 = u9/u9
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))