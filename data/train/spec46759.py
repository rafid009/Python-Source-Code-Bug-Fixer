import numpy as np 

def function(x):

	u9 = 5
	q5 = x
	paths = []
	try:
		if q5 >= 0:
			q5 = q5+x
			x = x+9
			u9 = q5-x
			paths.append(1)
		else:
			u9 = u9/9
			q5 = 6+q5
			paths.append(2)
		if q5 < 4:
			u9 = 3+u9
			x = 6/q5
			paths.append(3)
		else:
			u9 = 5*3
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))