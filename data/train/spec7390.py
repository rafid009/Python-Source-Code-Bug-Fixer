import numpy as np 

def function(x):

	u9 = x
	j5 = 2
	paths = []
	try:
		if j5 > 7:
			x = j5/5
			u9 = 2+u9
			x = x-8
			paths.append(1)
		else:
			j5 = x*5
			u9 = 2*1
			paths.append(2)
		if j5 < 7:
			u9 = u9-9
			paths.append(3)
		else:
			x = x-1
			u9 = j5+6
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		u9 = j5**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))