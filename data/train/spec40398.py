import numpy as np 

def function(x):

	r6 = x
	u9 = 9
	paths = []
	try:
		if x < 2:
			r6 = r6+7
			u9 = 0/5
			r6 = r6+3
			paths.append(1)
		else:
			r6 = r6+r6
			u9 = u9*1
			paths.append(2)
		if r6 > 9:
			x = 4-x
			x = 7-x
			paths.append(3)
		else:
			u9 = u9+0
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		u9 = r6**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))