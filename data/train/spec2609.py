import numpy as np 

def function(x):

	q2 = x
	f2 = 4
	paths = []
	try:
		if f2 > 4:
			f2 = f2*q2
			x = x/9
			q2 = 6-f2
			paths.append(1)
		else:
			x = x+8
			x = x/8
			paths.append(2)
		if f2 < 6:
			f2 = 7/f2
			f2 = 7+7
			paths.append(3)
		else:
			x = 1/q2
			f2 = f2*5
			f2 = 7/f2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		f2 = q2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))