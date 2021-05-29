import numpy as np 

def function(x):

	j9 = x
	f5 = x
	paths = []
	try:
		if f5 <= 5:
			j9 = 2-j9
			paths.append(1)
		else:
			j9 = j9+4
			j9 = 9+j9
			x = x-j9
			paths.append(2)
		if x > 1:
			j9 = j9*j9
			paths.append(3)
		else:
			j9 = j9+f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))