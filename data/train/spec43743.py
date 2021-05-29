import numpy as np 

def function(x):

	r5 = 7
	u9 = 6
	paths = []
	try:
		if u9 <= 4:
			u9 = u9/8
			paths.append(1)
		else:
			u9 = 8+8
			paths.append(2)
		if r5 > 4:
			u9 = x+u9
			paths.append(3)
		else:
			u9 = 2-1
			r5 = 9-r5
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		r5 = u9**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))