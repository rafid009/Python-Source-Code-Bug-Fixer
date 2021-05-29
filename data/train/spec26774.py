import numpy as np 

def function(x):

	i9 = 1
	u6 = 4
	paths = []
	try:
		if u6 > 0:
			u6 = x/6
			paths.append(1)
		else:
			i9 = 7-i9
			i9 = u6-i9
			paths.append(2)
		if x <= 1:
			i9 = i9+1
			u6 = x+u6
			u6 = 4*8
			paths.append(3)
		else:
			i9 = x/3
			u6 = 5-i9
			x = x+i9
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))