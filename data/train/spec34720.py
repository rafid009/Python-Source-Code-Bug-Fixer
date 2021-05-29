import numpy as np 

def function(x):

	t9 = x
	u7 = 7
	x = 7
	paths = []
	try:
		if u7 <= 7:
			u7 = u7+t9
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if t9 < 4:
			u7 = 4*u7
			paths.append(3)
		else:
			u7 = u7/9
			x = 9/u7
			u7 = 5+0
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))