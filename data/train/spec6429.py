import numpy as np 

def function(x):

	f8 = x
	t7 = x
	paths = []
	try:
		if f8 < 4:
			f8 = x*1
			t7 = t7+f8
			paths.append(1)
		else:
			t7 = t7/6
			paths.append(2)
		if f8 <= 6:
			f8 = 3+f8
			t7 = t7*t7
			t7 = 9/2
			paths.append(3)
		else:
			f8 = f8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))