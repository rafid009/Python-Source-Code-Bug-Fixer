import numpy as np 

def function(x):

	u7 = x
	b9 = 8
	paths = []
	try:
		if u7 > 5:
			u7 = x*4
			u7 = u7-b9
			paths.append(1)
		else:
			u7 = u7+x
			x = x+x
			paths.append(2)
		if x >= 6:
			x = x/8
			u7 = 5-2
			u7 = b9/3
			paths.append(3)
		else:
			x = 2*8
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		b9 = u7**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))