import numpy as np 

def function(x):

	u5 = x
	u9 = x
	x = 1
	paths = []
	try:
		if u5 < 2:
			u5 = u5-6
			u9 = u9/7
			paths.append(1)
		else:
			u9 = u5*0
			u9 = u9+4
			x = x+u5
			paths.append(2)
		if x > 0:
			x = 2*x
			paths.append(3)
		else:
			u5 = 1*u5
			u5 = 8*8
			u9 = 0+u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u5 = u9**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))