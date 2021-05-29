import numpy as np 

def function(x):

	u9 = x
	k7 = 0
	paths = []
	try:
		if x < 4:
			x = k7+x
			paths.append(1)
		else:
			k7 = k7/6
			u9 = 2/u9
			k7 = x*7
			paths.append(2)
		if k7 <= 7:
			u9 = u9/1
			k7 = k7+x
			u9 = 6*k7
			paths.append(3)
		else:
			k7 = k7/9
			x = x+7
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		k7 = u9**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))