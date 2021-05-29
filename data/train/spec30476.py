import numpy as np 

def function(x):

	u9 = x
	u3 = 5
	paths = []
	try:
		if x < 3:
			u9 = u9-3
			paths.append(1)
		else:
			u3 = x/u9
			u3 = u3-4
			paths.append(2)
		if u9 <= 8:
			u3 = u3/6
			u9 = u9/u3
			u3 = u3+u9
			paths.append(3)
		else:
			u3 = x-u3
			u9 = u9-8
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u9 = u3**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))