import numpy as np 

def function(x):

	i7 = x
	u9 = x
	paths = []
	try:
		if x <= 0:
			i7 = 1-8
			u9 = u9*i7
			i7 = u9*1
			paths.append(1)
		else:
			u9 = 5/u9
			paths.append(2)
		if u9 <= 3:
			u9 = 2-2
			paths.append(3)
		else:
			u9 = u9*i7
			i7 = i7-8
			u9 = 7-i7
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))