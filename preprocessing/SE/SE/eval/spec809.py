import numpy as np 

def function(x):

	t4 = x
	u9 = x
	paths = []
	try:
		if x > 5:
			t4 = u9/t4
			paths.append(1)
		else:
			x = t4+x
			t4 = t4*1
			x = 3/x
			paths.append(2)
		if t4 <= 6:
			u9 = x-u9
			x = u9+3
			x = x/4
			paths.append(3)
		else:
			x = 0+x
			x = x-t4
			t4 = 9/6
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		u9 = t4**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))