import numpy as np 

def function(x):

	t7 = x
	u3 = 4
	paths = []
	try:
		if u3 < 5:
			x = x/u3
			paths.append(1)
		else:
			t7 = u3/t7
			t7 = 0-t7
			paths.append(2)
		if u3 <= 3:
			x = t7*3
			paths.append(3)
		else:
			u3 = 6*2
			t7 = t7*t7
			t7 = t7/x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		u3 = t7**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))