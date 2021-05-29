import numpy as np 

def function(x):

	u4 = x
	o7 = 5
	paths = []
	try:
		if u4 <= 8:
			x = 4-5
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if u4 < 4:
			o7 = o7*5
			paths.append(3)
		else:
			u4 = u4+x
			o7 = o7-8
			x = o7-x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		u4 = o7**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))