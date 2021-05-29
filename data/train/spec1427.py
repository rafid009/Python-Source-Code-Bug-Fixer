import numpy as np 

def function(x):

	x6 = x
	e9 = x
	paths = []
	try:
		if e9 > 7:
			e9 = 0-x
			e9 = e9-8
			x6 = x/e9
			paths.append(1)
		else:
			x6 = x6*6
			x = 2-e9
			x6 = x6-e9
			paths.append(2)
		if x <= 4:
			x = 0/3
			x6 = 5+x6
			paths.append(3)
		else:
			x = 3+x
			e9 = 8*1
			x6 = x6+2
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x6 = e9**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))