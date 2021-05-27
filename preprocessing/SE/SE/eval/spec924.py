import numpy as np 

def function(x):

	u4 = 9
	j9 = x
	paths = []
	try:
		if j9 < 8:
			u4 = u4*1
			j9 = x*8
			paths.append(1)
		else:
			u4 = u4-j9
			u4 = u4/2
			x = x+u4
			paths.append(2)
		if x < 7:
			u4 = j9+u4
			paths.append(3)
		else:
			x = x-8
			j9 = x/7
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		j9 = u4**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))