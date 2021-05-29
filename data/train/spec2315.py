import numpy as np 

def function(x):

	v5 = x
	u5 = 4
	paths = []
	try:
		if x >= 5:
			u5 = 0/u5
			paths.append(1)
		else:
			u5 = u5-5
			paths.append(2)
		if x < 8:
			v5 = v5/1
			v5 = x-v5
			u5 = u5*7
			paths.append(3)
		else:
			v5 = v5-u5
			x = x*1
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		v5 = u5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))