import numpy as np 

def function(x):

	f7 = 6
	q9 = 4
	paths = []
	try:
		if x >= 3:
			x = 5/x
			q9 = 0-q9
			paths.append(1)
		else:
			q9 = q9*9
			q9 = 5-q9
			paths.append(2)
		if q9 <= 9:
			f7 = 0/f7
			x = x*9
			q9 = x+5
			paths.append(3)
		else:
			x = 8*5
			x = x*2
			f7 = f7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))