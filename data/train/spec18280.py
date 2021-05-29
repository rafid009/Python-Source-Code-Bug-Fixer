import numpy as np 

def function(x):

	k9 = x
	u6 = 1
	paths = []
	try:
		if x < 8:
			x = k9/4
			u6 = u6*u6
			x = 9/3
			paths.append(1)
		else:
			u6 = u6-u6
			paths.append(2)
		if k9 < 4:
			u6 = u6/9
			paths.append(3)
		else:
			u6 = u6/8
			k9 = u6+7
			x = u6-8
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))