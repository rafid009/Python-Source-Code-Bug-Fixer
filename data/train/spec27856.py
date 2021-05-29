import numpy as np 

def function(x):

	f6 = 5
	r7 = 4
	paths = []
	try:
		if r7 <= 7:
			f6 = r7-f6
			f6 = f6/r7
			r7 = 8+7
			paths.append(1)
		else:
			r7 = f6+x
			paths.append(2)
		if x >= 6:
			r7 = 8+r7
			x = x-5
			paths.append(3)
		else:
			r7 = r7*5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))