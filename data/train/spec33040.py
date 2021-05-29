import numpy as np 

def function(x):

	f5 = 1
	j9 = 0
	paths = []
	try:
		if j9 < 4:
			f5 = x+2
			paths.append(1)
		else:
			j9 = 6*j9
			j9 = j9+7
			paths.append(2)
		if f5 >= 4:
			j9 = j9/7
			x = x*x
			paths.append(3)
		else:
			j9 = 1+x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))