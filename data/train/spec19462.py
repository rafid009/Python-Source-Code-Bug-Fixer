import numpy as np 

def function(x):

	f4 = x
	l4 = 2
	paths = []
	try:
		if x <= 2:
			x = 7-f4
			l4 = 0+0
			x = 4-x
			paths.append(1)
		else:
			x = l4/2
			f4 = l4-f4
			paths.append(2)
		if l4 <= 5:
			l4 = 7/7
			l4 = f4+l4
			paths.append(3)
		else:
			f4 = 4+f4
			l4 = f4/3
			x = 2-5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))