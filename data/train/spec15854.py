import numpy as np 

def function(x):

	v0 = 5
	u9 = 6
	paths = []
	try:
		if u9 < 8:
			v0 = v0/7
			paths.append(1)
		else:
			v0 = v0*2
			v0 = 8/v0
			u9 = u9/7
			paths.append(2)
		if x > 4:
			x = 4/2
			paths.append(3)
		else:
			x = x+7
			x = x+9
			v0 = v0-4
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		u9 = v0**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))