import numpy as np 

def function(x):

	x6 = x
	u6 = 7
	paths = []
	try:
		if u6 > 2:
			u6 = u6-9
			u6 = u6+x6
			x6 = x6-9
			paths.append(1)
		else:
			u6 = u6-0
			x6 = x6*3
			x6 = x6+0
			paths.append(2)
		if x6 > 4:
			x6 = u6+3
			x6 = x6-6
			u6 = u6/4
			paths.append(3)
		else:
			u6 = 8+7
			x6 = x6/8
			x6 = x6/1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))