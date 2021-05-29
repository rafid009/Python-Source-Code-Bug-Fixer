import numpy as np 

def function(x):

	q8 = x
	u9 = 1
	paths = []
	try:
		if q8 < 3:
			q8 = x*9
			paths.append(1)
		else:
			u9 = 2/9
			paths.append(2)
		if x <= 2:
			u9 = u9+2
			u9 = 2-u9
			u9 = x/5
			paths.append(3)
		else:
			x = x*2
			q8 = q8+1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		q8 = u9**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))