import numpy as np 

def function(x):

	u1 = 2
	t7 = 7
	paths = []
	try:
		if u1 <= 3:
			u1 = 1+u1
			u1 = 2*9
			t7 = 2-t7
			paths.append(1)
		else:
			u1 = t7-u1
			x = 9+x
			paths.append(2)
		if u1 < 5:
			t7 = 5/t7
			u1 = 2*u1
			t7 = t7/4
			paths.append(3)
		else:
			u1 = 7-4
			x = 1+t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))