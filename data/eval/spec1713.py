import numpy as np 

def function(x):

	t7 = 5
	f7 = 3
	paths = []
	try:
		if x <= 3:
			t7 = t7+4
			paths.append(1)
		else:
			x = x+t7
			paths.append(2)
		if x <= 6:
			t7 = 3-t7
			x = x*1
			paths.append(3)
		else:
			f7 = 2-2
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		f7 = t7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))