import numpy as np 

def function(x):

	f4 = 4
	q9 = x
	paths = []
	try:
		if q9 <= 0:
			q9 = q9*1
			paths.append(1)
		else:
			f4 = f4+7
			paths.append(2)
		if x < 2:
			x = q9/x
			x = 1+0
			f4 = x+q9
			paths.append(3)
		else:
			q9 = f4*4
			q9 = 0*q9
			x = x-0
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