import numpy as np 

def function(x):

	u7 = x
	t5 = x
	paths = []
	try:
		if x <= 3:
			u7 = u7+5
			paths.append(1)
		else:
			t5 = t5-6
			x = x/3
			paths.append(2)
		if t5 <= 4:
			x = x+0
			u7 = u7+u7
			paths.append(3)
		else:
			t5 = 1+u7
			t5 = t5-u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))