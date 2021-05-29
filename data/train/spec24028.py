import numpy as np 

def function(x):

	f5 = 5
	t9 = 1
	paths = []
	try:
		if f5 > 7:
			f5 = 4/x
			x = x*7
			f5 = t9/1
			paths.append(1)
		else:
			t9 = t9*1
			x = x+0
			x = 8-x
			paths.append(2)
		if f5 >= 4:
			t9 = f5-9
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))