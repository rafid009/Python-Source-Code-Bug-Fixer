import numpy as np 

def function(x):

	q3 = x
	u9 = x
	paths = []
	try:
		if q3 <= 3:
			u9 = u9+u9
			q3 = q3+7
			paths.append(1)
		else:
			u9 = u9+9
			x = 2/x
			paths.append(2)
		if u9 >= 4:
			u9 = q3*q3
			x = u9-q3
			q3 = 8+q3
			paths.append(3)
		else:
			x = x*0
			q3 = 9/q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))