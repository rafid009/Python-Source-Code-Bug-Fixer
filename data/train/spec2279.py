import numpy as np 

def function(x):

	x6 = 3
	f5 = x
	paths = []
	try:
		if x6 < 5:
			x6 = x6+x
			x6 = x6*2
			paths.append(1)
		else:
			f5 = x6-9
			x = f5/1
			f5 = x+1
			paths.append(2)
		if x < 5:
			x = x-8
			paths.append(3)
		else:
			x6 = 9+x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		f5 = x6**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))