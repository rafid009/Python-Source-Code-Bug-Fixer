import numpy as np 

def function(x):

	q2 = 4
	f9 = 9
	paths = []
	try:
		if x < 2:
			f9 = 1-f9
			q2 = x/q2
			paths.append(1)
		else:
			f9 = f9+9
			q2 = q2+x
			paths.append(2)
		if f9 > 5:
			f9 = x-f9
			q2 = q2*q2
			q2 = x/f9
			paths.append(3)
		else:
			q2 = f9/q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		f9 = q2**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))